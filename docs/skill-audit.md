# Imported Blender skill audit

Targeted safety, portability and API corrections preserve the five imports' trigger
intent and substantive recipes. Start review with the
[shared runtime gates](../.agents/skills/BLENDER_RUNTIME.md), then compare recipes.

## Findings and local adaptations

| Skill | Actionable finding | Applied correction |
|---|---|---|
| Blender / Flue | Author-private Windows path; implied Flue exclusivity; Photoshop payload instead of promised bpy example | Host-discovered installation paths; connected MCP supported without Flue; optional Flue prerequisites and read-only bpy payload |
| blender-animation | Missing backend prerequisite; overview's legacy-only F-curves; all-channelbag helper could edit other objects | Shared runtime pointer; overview uses compatibility helper; helper filters the object's assigned action slot and retains legacy handling |
| blender-modeling | Missing backend prerequisite; absent companion skills; invalid `from_pymesh` name; operator-context-sensitive cleanup | Explicit optional/unavailable branch; documented BMesh load/write/free lifecycle; single-user Object Mode cleanup via BMesh |
| blender-rendering | Missing backend prerequisite; absent calibration skill; legacy EEVEE reference; unsupported temporal promise; machine-wide GPU edits; arbitrary camera and fixed outputs | Runtime discovery/forecast; optional calibration branch; reference points to guarded Recipe 3; unsupported temporal switch removed; read-only device inspection; intended-camera guard and checked illustrative outputs |
| blender-export | Whole-scene defaults; mutating preflight; automatic texture overwrite; fixed outputs; universalized GLB/PNG budgets; stale USD keyword | Selection-scoped flags in every format example; read-only preflight and export-copy rule; texture overwrite disabled; approved destinations required; project-specific budgets; gated 5.2 USD texture mode |

All five descriptions are YAML-safe quoted strings with original activation
examples retained. Legacy host-specific tool allowlists were removed: only the
current host grants tool permissions. Each main skill and operational reference
points to shared permission/object/output gates. Missing `wireframe-to-3d`,
`blender-materials`, `blender-pro-workflow` and `reference-look-calibration` were
not imported; agents stop only the affected branch and report the gap.

Export snippets are settings examples, not standalone selection/path wrappers.
The shared contract requires intended-object confirmation, temporary-context
restoration, absolute approved output destinations, sidecar/texture checks,
source-save/export-copy precautions and explicit existing-file overwrite consent.
Bundled collision/bake helpers already reject existing files and preserve temporary
context; their source and those invariants remain unchanged.

## Provenance and licensing limits

- Import evidence is `skills-lock.json`: Flue from `sfkislev/flue`, four domain
  skills from `roble3/cc-blender-skill`, with original import paths and computed
  hashes. It contains **no upstream revision**. It remains unchanged; its hashes
  do not verify locally adapted files or establish a reproducible upstream version.
- The audit used a local-only snapshot of the unmodified imports; the tracked
  starter commit does not contain those imports. Committed tests do not depend
  on that history or snapshot. Differential reproduction requires your own copy
  of the original imports, supplied through `IMPORT_BASELINE` below.
- [Scoped full MIT notices](../THIRD_PARTY_NOTICES.md) reproduce the public license
  texts fetched read-only on 2026-11-05, with 2026 SFKislev and 2026 RobLe3 notices.
  These public `main` URLs are not pinned evidence of the imported revision.
  No repository-wide license, upstream version or upstream validation was invented.
- Canonical `.agents/skills/` files remain real files; the five `.claude/skills/`
  aliases remain relative symlinks. Evals and Python helpers are preserved.

## Verification evidence and limits

Structural tests assert actionable contracts, not stylistic word counts or Blender
execution. Existing eval JSON contains trigger examples, not an invocation runner
or runtime correctness tests. No CLI/options were added, so command exit/stdout/
stderr regression matrices are inapplicable; recipe-level differential probes and
import byte comparisons provide proportionate preservation evidence instead.

| Check | Observed result |
|---|---|
| Initial structural RED | 16 tests; 31 failing subtests and 5 unquoted-description JSON errors; two preservation tests passed |
| First post-fix structural run | One test-parser false positive mistook Python `helpers['name'](...)` for a Markdown link; parser corrected to exclude code |
| Structural GREEN before additional USD discovery | 16 tests passed |
| USD-specific RED | Added regression test failed on obsolete `export_textures` keyword; isolated Blender RNA probe independently rejected that keyword |
| Final structural run | 18 tests passed with the required bytecode-disabled command; all known local Markdown links and imported eval JSON validated |
| Independent verification | No technical blockers; isolated scope/rejection probes passed, with unchanged state hashes after rejected operations |
| Bundled Python syntax | Exit 0: `Bundled helper syntax OK`; parses helpers without importing bpy or executing them |
| Initial isolated API probe | Blender 5.2.3 LTS; layered Actions; current exporter selection flags available; `BLENDER_EEVEE_NEXT` rejected; `BLENDER_EEVEE` accepted; no `denoising_use_animation` |
| Recipe differential | Single-slot F-curves: 3 before/after; two-slot action: baseline helper returns 6, scoped helper returns 3 per object; cleanup preserves 8 vertices/6 smooth faces on a cube; guarded EEVEE preset has equal output before/after |
| Export keyword introspection | All documented general exporter keyword names exist in installed RNA after USD correction; no actual export or target-app import performed |
| Import preservation comparison | Lock, four eval files, two helpers and five alias targets byte-for-byte unchanged; all five trigger descriptions retained (modeling adds only an optional-companion qualifier); all Python snippets parse |

**Correction to the explorer's hypothesis:** `normals_make_consistent` is still
registered in this installed 5.2.3 build and the baseline cleanup executed. BMesh
is used for explicit mesh scope and context independence, not because removal was
proved. Likewise `denoising_input_passes` exists here, but does not establish temporal
animation denoising without the absent switch. Context7's mixed-version API index
also returned the normals operator; installed introspection settled local behavior.

Official documentation consulted through Context7: Blender Python API
(`/websites/blender_api`) on Action slots/channelbags, BMesh from/to-mesh lifecycle,
normal recalculation and USD texture modes; Blender Manual
(`/websites/blender_manual_en`) on EEVEE ray-tracing/denoising and engine limitations.
These are references, not exhaustive version certification.

`tests/test_recipe_runtime.py` retains the independent probes for slot isolation,
bounded cleanup, rejection-state preservation, read-only preflight and missing-camera
guards. It runs a factory-startup background Blender process, not the live scene,
and skips explicitly when Blender is unavailable. This is not a full exporter test.

**Untested:** live MCP transport/addon connectivity, Flue installation/bridge command,
GPU rendering and device setup, actual still/animation renders, file overwrite
handling in Blender exporters, non-cube topology, legacy Blender releases, full
Multires baking, rigged exports and Unreal/Unity/web/AR importer acceptance. The
imported 5.1.1 bake-validation claim is explicitly labeled upstream-reported, not
reproduced here. No live scene, GPU preferences, render or export files were changed.

## Remaining style advisories

Long descriptions, tutorial-sized bodies, broad artistic heuristics, upstream
status dates, outstanding checklists and nonuniform section order remain advisory.
Shortening them to the house token budget would risk losing upstream triggers or
meaningful recipes. No fabricated `metadata.version` was added. Future work can
disclose recipes progressively with separate scope and full runtime validation;
this audit intentionally avoids a wholesale rewrite or new dependencies.

## Reproduction commands

Run from the repository root. Required checks:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 -c "import ast,pathlib; [ast.parse(p.read_text()) for p in pathlib.Path('.agents/skills').rglob('*.py')]; print('Bundled helper syntax OK')"
```

The factory-startup probe below uses an isolated HOME/cache/temp directory. It
does not save scenes, render, export, install, access remote services or write GPU
preferences. It prints its scratch directory so you can remove it after use.
Set `IMPORT_BASELINE` to an absolute directory containing an unmodified `.agents/`
import tree; this external comparison input is not bundled with the repository.

```sh
: "${IMPORT_BASELINE:?Set IMPORT_BASELINE to your original import directory}"
export IMPORT_BASELINE
scratch=$(mktemp -d "${TMPDIR:-/tmp}/blender-recipe-probe.XXXXXX"); printf 'Scratch: %s\n' "$scratch"; HOME="$scratch" TMPDIR="$scratch" XDG_CONFIG_HOME="$scratch" XDG_CACHE_HOME="$scratch" blender --background --factory-startup --disable-autoexec --python-exit-code 1 --python-expr "exec(__import__('sys').stdin.read())" <<'PY'
import ast, bpy, bmesh, os, pathlib, re
current = pathlib.Path('.agents/skills')
baseline = pathlib.Path(os.environ['IMPORT_BASELINE']) / '.agents/skills'
def recipe(root, skill, number):
    text = (root / skill / 'SKILL.md').read_text().split(f'### Recipe {number} ')[1]
    return re.search(r'```python\n(.*?)```', text, re.S).group(1)
def helper(root):
    tree = ast.parse(recipe(root, 'blender-animation', 3))
    tree.body = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    scope = {}
    exec(compile(tree, '<animation helper>', 'exec'), scope)
    return scope['get_fcurves_compat']
obj = bpy.data.objects['Cube']
obj.keyframe_insert('location', frame=1)
old, new = helper(baseline), helper(current)
assert len(old(obj.animation_data.action)) == len(new(obj)) == 3
print('PRESERVE_SINGLE_SLOT', 3)
other = obj.copy()
bpy.context.collection.objects.link(other)
action = obj.animation_data.action
slot = action.slots.new(id_type='OBJECT', name='Other')
other.animation_data.action_slot = slot
other.keyframe_insert('location', frame=1)
assert len(old(action)) == 6 and len(new(obj)) == len(new(other)) == 3
print('MULTI_SLOT_BASELINE_CURRENT', len(old(action)), len(new(obj)))
for label, root in [('baseline', baseline), ('current', current)]:
    mesh = bpy.data.meshes.new(label)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=2)
    bm.to_mesh(mesh)
    bm.free()
    target = bpy.data.objects.new('GEO-target', mesh)
    bpy.context.collection.objects.link(target)
    bpy.ops.object.select_all(action='DESELECT')
    target.select_set(True)
    bpy.context.view_layer.objects.active = target
    exec(recipe(root, 'blender-modeling', 8), {})
    assert (len(mesh.vertices), len(mesh.polygons)) == (8, 6)
    assert all(p.use_smooth for p in mesh.polygons)
    print('CLEANUP_PRESERVE', label, len(mesh.vertices), len(mesh.polygons))
    target.name = label
for label, root in [('baseline', baseline), ('current', current)]:
    exec(recipe(root, 'blender-rendering', 3), {})
    print('EEVEE_PRESERVE', label, bpy.context.scene.render.engine)
for path in (current / 'blender-export').rglob('*.md'):
    for block in re.findall(r'^```python\n(.*?)^```', path.read_text(), re.M | re.S):
        for node in ast.walk(ast.parse(block)):
            if not isinstance(node, ast.Call):
                continue
            name = ast.unparse(node.func)
            if name.count('.') == 3 and name.startswith(('bpy.ops.export_scene.', 'bpy.ops.wm.')):
                op = eval(name)
                props = op.get_rna_type().properties
                assert all(k.arg in props for k in node.keywords), (name, [k.arg for k in node.keywords if k.arg not in props])
print('EXPORT_KEYWORDS_OK')
print('RECIPE_PROBE_OK_NO_RENDER_OR_EXPORT')
PY
```

Probe history: first attempt found obsolete USD `export_textures`; after that fix,
the probe's own scanner mistook `get_rna_type()` for an exporter. Restricting it to
operator-level calls fixed the harness. Final command above exited 0 with
`EXPORT_KEYWORDS_OK` and `RECIPE_PROBE_OK_NO_RENDER_OR_EXPORT`.

Initial API introspection command (exit 0, `PROBE_OK`):

```sh
scratch=$(mktemp -d "${TMPDIR:-/tmp}/blender-skill-probe.XXXXXX"); printf 'Scratch: %s\n' "$scratch"; HOME="$scratch" TMPDIR="$scratch" XDG_CONFIG_HOME="$scratch" XDG_CACHE_HOME="$scratch" blender --background --factory-startup --disable-autoexec --python-exit-code 1 --python-expr "exec(__import__('sys').stdin.read())" <<'PY'
import bpy, bmesh, json
scene = bpy.context.scene
print('VERSION', bpy.app.version_string)
for path in ('normals_make_consistent', 'remove_doubles'):
    try:
        getattr(bpy.ops.mesh, path).get_rna_type()
        print('MESH_OP', path, True)
    except (KeyError, RuntimeError):
        print('MESH_OP', path, False)
print('BMESH', hasattr(bmesh.types.BMesh, 'from_mesh'), hasattr(bmesh.ops, 'recalc_face_normals'))
obj = bpy.data.objects['Cube']
obj.keyframe_insert('location', frame=1)
obj.location.z = 1
obj.keyframe_insert('location', frame=2)
action = obj.animation_data.action
print('ACTION', hasattr(action, 'fcurves'), hasattr(action, 'layers'), obj.animation_data.action_slot.handle)
print('CHANNELBAGS', [(cb.slot_handle, len(cb.fcurves)) for l in action.layers for s in l.strips for cb in s.channelbags])
for engine in ('BLENDER_EEVEE_NEXT', 'BLENDER_EEVEE', 'CYCLES'):
    try:
        scene.render.engine = engine
        print('ENGINE', engine, True)
    except (TypeError, ValueError):
        print('ENGINE', engine, False)
print('LEGACY_EEVEE', {p: hasattr(getattr(scene, 'eevee', None), p) for p in ('taa_render_samples', 'taa_samples', 'use_gtao', 'use_bloom', 'use_ssr')})
print('TEMPORAL', {p: hasattr(scene.cycles, p) for p in ('denoising_use_animation', 'denoising_input_passes')})
for namespace, name, flag in [('export_scene','gltf','use_selection'), ('export_scene','fbx','use_selection'), ('wm','obj_export','export_selected_objects'), ('wm','stl_export','export_selected_objects'), ('wm','usd_export','selected_objects_only')]:
    op = getattr(getattr(bpy.ops, namespace), name)
    props = op.get_rna_type().properties
    assert flag in props, (name, flag)
    print('EXPORT_SCOPE', name, flag)
print('PROBE_OK')
PY
```

One-off import preservation check (exit 0):

```sh
: "${IMPORT_BASELINE:?Set IMPORT_BASELINE to your original import directory}"
export IMPORT_BASELINE
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import ast, json, os, pathlib, re
root = pathlib.Path('.')
base = pathlib.Path(os.environ['IMPORT_BASELINE'])
assert (root / 'skills-lock.json').read_bytes() == (base / 'skills-lock.json').read_bytes()
unchanged = list((base / '.agents/skills').glob('*/evals/evals.json')) + list((base / '.agents/skills').glob('*/scripts/*.py'))
for path in unchanged:
    assert path.read_bytes() == (root / path.relative_to(base)).read_bytes(), path
for path in (base / '.agents/skills').glob('*/SKILL.md'):
    old = re.search(r'^description: (.+)$', path.read_text(), re.M).group(1)
    text = (root / path.relative_to(base)).read_text()
    new = json.loads(re.search(r'^description: (.+)$', text, re.M).group(1))
    assert new.replace('Pairs with optional ', 'Pairs with ') == old, path
    assert re.search(r'^name: (.+)$', path.read_text(), re.M).group(1) == re.search(r'^name: (.+)$', text, re.M).group(1)
for path in (base / '.claude/skills').iterdir():
    assert (root / path.relative_to(base)).readlink() == path.readlink()
for path in (root / '.agents/skills').rglob('*.md'):
    for block in re.findall(r'^```python\n(.*?)^```', path.read_text(), re.M | re.S):
        ast.parse(block)
print('Snapshot comparison OK: lock, 4 evals, 2 helpers, 5 aliases unchanged; all 5 trigger descriptions retained; Python snippets parse')
PY
```
