"""Exercise adapted recipes in disposable Blender state, never the live scene."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

PROBE = r'''
import ast, bpy, hashlib, json, pathlib, re

def recipe(skill, number):
    text = (pathlib.Path('.agents/skills') / skill / 'SKILL.md').read_text()
    text = text.split(f'### Recipe {number} ')[1]
    return re.search(r'^```python\n(.*?)^```', text, re.M | re.S).group(1)

def definitions(code):
    tree = ast.parse(code)
    tree.body = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    scope = {}
    exec(compile(tree, '<recipe>', 'exec'), scope)
    return scope

def snapshot():
    scene = bpy.context.scene
    state = {
        'objects': [(o.name, o.mode, o.select_get(), o.data.name if o.data else None,
                     tuple(o.location), tuple(o.scale)) for o in bpy.data.objects],
        'meshes': [(m.name, [tuple(v.co) for v in m.vertices],
                    [(tuple(p.vertices), p.use_smooth) for p in m.polygons])
                   for m in bpy.data.meshes],
        'active': bpy.context.view_layer.objects.active.name,
        'camera': scene.camera.name if scene.camera else None,
        'render': (scene.render.engine, scene.render.filepath,
                   scene.render.image_settings.file_format),
        'actions': [(a.name, [(cb.slot_handle,
                     [(fc.data_path, fc.array_index,
                       [(tuple(k.co), k.interpolation) for k in fc.keyframe_points])
                      for fc in cb.fcurves])
                     for layer in a.layers for strip in layer.strips
                     for cb in strip.channelbags]) for a in bpy.data.actions],
    }
    return hashlib.sha256(json.dumps(state, sort_keys=True).encode()).hexdigest()

def reject(operation, error_type, message):
    before = snapshot()
    try:
        operation()
    except error_type as error:
        assert str(error) == message, str(error)
    else:
        raise AssertionError('Operation unexpectedly accepted')
    assert snapshot() == before, 'Rejected operation changed state'

curves = definitions(recipe('blender-animation', 3))['get_fcurves_compat']
obj = bpy.data.objects['Cube']
obj.name = 'GEO-target'
obj.keyframe_insert('location', frame=1)
obj.keyframe_insert('location', frame=2)
other = obj.copy()
other.data = obj.data.copy()
bpy.context.collection.objects.link(other)
other.name = 'Other'
other.animation_data.action_slot = obj.animation_data.action.slots.new(
    id_type='OBJECT', name='Other')
other.keyframe_insert('location', frame=1)
before = [k.interpolation for fc in curves(other) for k in fc.keyframe_points]
assert len(curves(obj)) == len(curves(other)) == 3
exec(recipe('blender-animation', 3), {})
assert all(k.interpolation == 'LINEAR'
           for fc in curves(obj) for k in fc.keyframe_points)
assert before == [k.interpolation for fc in curves(other) for k in fc.keyframe_points]
obj.animation_data.action_slot = None
reject(lambda: curves(obj), ValueError, 'Layered Action has no assigned slot')
obj.animation_data_clear()
assert curves(obj) == []

cleanup = recipe('blender-modeling', 8)
bpy.ops.object.select_all(action='DESELECT')
other.select_set(True)
bpy.context.view_layer.objects.active = other
before = ([tuple(v.co) for v in other.data.vertices],
          [p.use_smooth for p in other.data.polygons])
exec(cleanup, {})
assert (len(obj.data.vertices), len(obj.data.polygons)) == (8, 6)
assert all(p.use_smooth for p in obj.data.polygons)
assert before == ([tuple(v.co) for v in other.data.vertices],
                  [p.use_smooth for p in other.data.polygons])
assert bpy.context.view_layer.objects.active == other and other.select_get()
linked = obj.copy()
bpy.context.collection.objects.link(linked)
reject(lambda: exec(cleanup, {}), ValueError,
       'Use an intended single-user mesh in Object Mode')
bpy.data.objects.remove(linked, do_unlink=True)
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)
bpy.context.view_layer.objects.active = obj
bpy.ops.object.mode_set(mode='EDIT')
reject(lambda: exec(cleanup, {}), ValueError,
       'Use an intended single-user mesh in Object Mode')
bpy.ops.object.mode_set(mode='OBJECT')
before = snapshot()
exec(recipe('blender-export', 7), {})
assert before == snapshot(), 'Export preflight mutated state'
for number in (5, 6):
    guard = definitions(recipe('blender-rendering', number))['ensure_camera']
    bpy.context.scene.camera = None
    reject(lambda: guard(bpy.context.scene), RuntimeError,
           'Confirm and assign the intended scene camera before rendering')
    bpy.context.scene.camera = bpy.data.objects['Camera']
    assert guard(bpy.context.scene) == 'Camera'
print('RECIPE_SCOPE_PROBES_OK')
'''


class RecipeRuntime(unittest.TestCase):
    @unittest.skipUnless(shutil.which('blender'), 'Blender unavailable')
    def test_adapted_recipe_scope_and_rejections(self):
        with tempfile.TemporaryDirectory(prefix='blender-skill-runtime-') as directory:
            env = dict(os.environ, HOME=directory, TMPDIR=directory,
                       XDG_CONFIG_HOME=directory, XDG_CACHE_HOME=directory,
                       PYTHONDONTWRITEBYTECODE='1')
            result = subprocess.run(
                ['blender', '--background', '--factory-startup', '--disable-autoexec',
                 '--python-exit-code', '1', '--python-expr',
                 "exec(__import__('sys').stdin.read())"],
                input=PROBE, text=True, capture_output=True, cwd=ROOT,
                env=env, timeout=120,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn('RECIPE_SCOPE_PROBES_OK', result.stdout)


if __name__ == '__main__':
    unittest.main()
