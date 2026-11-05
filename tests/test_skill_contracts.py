"""Structural documentation contracts, not proof of Blender runtime behavior."""
import ast
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents/skills'
NAMES = ('blender', 'blender-animation', 'blender-modeling',
         'blender-rendering', 'blender-export')


def documents(name):
    return sorted((SKILLS / name).rglob('*.md'))


def python_blocks(path):
    return re.findall(r'^```python\n(.*?)^```', path.read_text(), re.M | re.S)


def calls(path):
    for block in python_blocks(path):
        yield from (n for n in ast.walk(ast.parse(block)) if isinstance(n, ast.Call))


def local_links(path):
    prose = re.sub(r'^```[^\n]*\n.*?^```', '', path.read_text(), flags=re.M | re.S)
    prose = re.sub(r'`[^`\n]+`', '', prose)
    return [target.split('#')[0] for target in re.findall(r'\]\(([^)]+)\)', prose)
            if '://' not in target and not target.startswith('#')]


class SkillContracts(unittest.TestCase):
    def test_backend_references_resolve(self):
        for name in NAMES:
            path = SKILLS / name / 'SKILL.md'
            with self.subTest(skill=name):
                self.assertIn('../BLENDER_RUNTIME.md', path.read_text())
                for target in local_links(path):
                    self.assertTrue((path.parent / target).is_file(), target)

    def test_supporting_local_links_resolve(self):
        paths = [p for name in NAMES for p in documents(name)]
        paths += [SKILLS / 'BLENDER_RUNTIME.md', ROOT / 'THIRD_PARTY_NOTICES.md',
                  ROOT / 'docs/skill-audit.md']
        for path in paths:
            self.assertTrue(path.is_file(), str(path))
            for target in local_links(path):
                self.assertTrue((path.parent / target).is_file(), f'{path}: {target}')

    def test_frontmatter_quotes_preserve_discovery(self):
        for name in NAMES:
            text = (SKILLS / name / 'SKILL.md').read_text()
            with self.subTest(skill=name):
                value = re.search(r'^description: (.+)$', text, re.M).group(1)
                self.assertIsInstance(json.loads(value), str)
                self.assertNotIn('allowed-tools:', text)

    def test_portable_flue_and_bpy_example(self):
        text = '\n'.join(p.read_text() for p in documents('blender'))
        self.assertNotRegex(text, r'[A-Za-z]:\\Users\\')
        self.assertNotIn('cannot act inside', text)
        example = '\n'.join(python_blocks(SKILLS / 'blender/FLUE.md'))
        self.assertIn('bpy.context.scene', example)
        self.assertNotIn('app.documents.add', text)

    def test_absent_handoffs_are_optional(self):
        text = '\n'.join(p.read_text() for n in NAMES for p in documents(n))
        self.assertNotIn('text-to-blender/references/mcp-backends.md', text)
        runtime = SKILLS / 'BLENDER_RUNTIME.md'
        self.assertTrue(runtime.is_file())
        text = runtime.read_text().lower()
        for missing in ('wireframe-to-3d', 'blender-materials',
                        'blender-pro-workflow', 'reference-look-calibration'):
            self.assertIn(missing, text)
        self.assertRegex(text, r'optional')
        self.assertRegex(text, r'stop.*branch')

    def test_shared_runtime_safety_gates(self):
        path = SKILLS / 'BLENDER_RUNTIME.md'
        self.assertTrue(path.is_file())
        text = path.read_text().lower()
        for topic in ('permission', 'read-only', 'addon', 'scene', 'intended objects',
                      'source', 'copy', 'overwrite', 'consent', 'remote', 'install',
                      'forecast', 'frame', 'resolution', 'sample'):
            self.assertIn(topic, text)

    def test_exports_are_selection_scoped(self):
        flags = {'gltf': 'use_selection', 'fbx': 'use_selection',
                 'obj_export': 'export_selected_objects',
                 'stl_export': 'export_selected_objects', 'usd_export': 'selected_objects_only'}
        seen = set()
        for path in documents('blender-export'):
            for call in calls(path):
                if isinstance(call.func, ast.Attribute) and call.func.attr in flags:
                    name = call.func.attr
                    seen.add(name)
                    values = {k.arg: k.value for k in call.keywords}
                    with self.subTest(path=path.name, exporter=name):
                        self.assertIn(flags[name], values)
                        self.assertIs(ast.literal_eval(values[flags[name]]), True)
                        if name == 'usd_export':
                            self.assertIs(ast.literal_eval(values['overwrite_textures']), False)
        self.assertEqual(seen, set(flags))

    def test_output_examples_have_no_fixed_tmp_paths(self):
        for name in NAMES:
            for path in documents(name):
                with self.subTest(path=path):
                    self.assertNotIn('/tmp/', path.read_text())

    def test_export_preflight_is_read_only(self):
        text = (SKILLS / 'blender-export/SKILL.md').read_text()
        preflight = text.split('### Recipe 7')[1].split('### Recipe 8')[0]
        self.assertNotIn('bpy.ops.', preflight)
        self.assertIn('copy', preflight.lower())

    def test_usd_texture_options_match_current_recipe(self):
        for path in documents('blender-export'):
            for call in calls(path):
                if isinstance(call.func, ast.Attribute) and call.func.attr == 'usd_export':
                    keys = {k.arg for k in call.keywords}
                    self.assertNotIn('export_textures', keys)
                    self.assertIn('export_textures_mode', keys)
                    self.assertIn('get_rna_type()', path.read_text())

    def test_current_mesh_api(self):
        for name in ('blender-modeling', 'blender-export'):
            for path in documents(name):
                self.assertNotIn('normals_make_consistent', path.read_text())
                self.assertNotIn('from_pymesh', path.read_text())
        self.assertIn('bmesh.ops.recalc_face_normals',
                      (SKILLS / 'blender-modeling/SKILL.md').read_text())

    def test_animation_overview_uses_layered_compatibility(self):
        text = (SKILLS / 'blender-animation/references/overview.md').read_text()
        self.assertNotIn('action.fcurves.find', text)
        self.assertIn('get_fcurves_compat', text)
        self.assertIn('slot', text.lower())

    def test_render_overview_gates_legacy_settings(self):
        text = (SKILLS / 'blender-rendering/references/overview.md').read_text()
        self.assertNotRegex(text, r'scene\.eevee\.\w+\s*=')
        self.assertNotIn('denoising_use_animation =', text)
        self.assertNotIn('denoising_input_passes =', text)
        self.assertIn('Recipe 3', text)

    def test_gpu_preferences_not_mutated_by_recipes(self):
        for path in documents('blender-rendering'):
            text = path.read_text()
            self.assertNotRegex(text, r'compute_device_type\s*=')
            self.assertNotRegex(text, r'device\.use\s*=')

    def test_gltf_budgets_not_universal_limits(self):
        for path in documents('blender-export'):
            text = path.read_text()
            self.assertNotRegex(text, r'(?i)hard cap.{0,8}15 MB|PNG textures only')
        self.assertIn('project guidance', (SKILLS / 'blender-export/SKILL.md').read_text())

    def test_full_scoped_mit_notices(self):
        path = ROOT / 'THIRD_PARTY_NOTICES.md'
        self.assertTrue(path.is_file())
        text = path.read_text()
        for owner in ('SFKislev', 'RobLe3'):
            self.assertIn(f'Copyright (c) 2026 {owner}', text)
        for clause in ('Permission is hereby granted, free of charge',
                       'The above copyright notice and this permission notice',
                       'THE SOFTWARE IS PROVIDED "AS IS"',
                       'SOFTWARE.'):
            self.assertEqual(text.count(clause), 2)
        for name in NAMES:
            self.assertIn(f'.agents/skills/{name}/', text)

    def test_preserve_aliases_and_support_files(self):
        for name in NAMES:
            alias = ROOT / '.claude/skills' / name
            self.assertTrue(alias.is_symlink())
            self.assertFalse(alias.readlink().is_absolute())
            self.assertEqual(alias.resolve(), (SKILLS / name).resolve())
        for helper in ('collision_preflight.py', 'multires_bake_export.py'):
            ast.parse((SKILLS / 'blender-export/scripts' / helper).read_text())

    def test_preserve_trigger_evaluation_data(self):
        paths = list(SKILLS.glob('*/evals/evals.json'))
        self.assertEqual(len(paths), 4)
        for path in paths:
            rows = json.loads(path.read_text())
            self.assertTrue(any(r['should_trigger'] for r in rows))
            self.assertTrue(any(not r['should_trigger'] for r in rows))
            for row in rows:
                self.assertIsInstance(row['query'], str)
                self.assertIs(type(row['should_trigger']), bool)


if __name__ == '__main__':
    unittest.main()
