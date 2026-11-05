# Bounded Blender prompt templates

Replace every `<placeholder>` before sending; these are example prompts, not
tested generated assets. Use the [workflow](modeling-workflow.md) and
[best practices](best-practices.md). Each prompt stands alone and stops at a review gate.

## Reference-based prop

```text
Create <prop> for <engine/use>, using the attached rights-cleared reference.
Observed: <silhouette, visible parts, colors, image-space proportions>.
Unknown: <hidden surfaces, construction, scale>. Proposed assumptions: <choices>.
Target: <dimensions and units>, <= <triangles> triangles, textures <= <pixels> px.
First inspect the scene and report observations separately from assumptions.
Ask about unresolved requirements; do not claim exact unseen geometry.
Confirm a new working-copy path <asset/source/name-v01.blend> and overwrite
permission before writing. Preserve the original and all existing scene objects;
do not delete or clear the live scene. Add work only in collection <collection>.
After approval, build only a simple blockout. Show reference-angle, side, and rear
previews, report dimensions and triangle count, and stop for silhouette approval.
Done for this stage: requested views shown, constraints checked, unknowns listed;
no detailed materials, export, or upload yet.
```

## Fruit scene refinement

```text
Refine the existing apple and pear in <collection> for <engine/use>.
First inspect and report their object names, dimensions, and triangle counts.
Target: <dimensions/units>, <= <triangles per fruit>, textures <= <pixels> px.
Revision: <one observable change, e.g. narrow the pear's upper body by 10%>.
Preserve the other fruit, stems, leaves, floor, camera, lights, and unrelated data.
Confirm a new saved copy <asset/source/fruit-v02.blend> and overwrite permission
before edits. Preserve the original; never delete or clear the live scene.
Ask if a named object or constraint is missing instead of substituting silently.
Show before/after previews from the same camera, plus a side view for contacts.
Done: requested change visible, parts meet without accidental intersections,
each fruit remains independently selectable, dimensions/budget checked.
List changed objects and stop for approval; do not export or upload.
```

## Material and lighting iteration

```text
Inspect <objects/materials> and propose one change to improve <observable goal>.
For this pass change only <material roughness/base color OR named light setting>;
hold geometry, camera, color management, and every other material/light fixed.
Confirm a new working-copy path <asset/source/look-v02.blend> and overwrite
permission before writing. Preserve the original and all scene objects; no deletion.
Ask before editing a shared material that would affect objects outside this scope.
Use shader inputs, not only viewport display colors. Capture before/after previews
with the same render settings. For <target engine>, flag procedural detail that
would need baking; do not promise Blender's appearance will export unchanged.
Done: show the comparison, list exact changed settings and portability limits,
then stop for approval. No geometry edits, baking, export, or upload in this pass.
```

## Selected asset GLB export

```text
Prepare only <explicit object names, including all stems/leaves> for GLB delivery
to <engine/version>. First inspect and report the exact export set, dimensions,
triangle count, texture sizes, missing files, and any unsupported materials.
Limits: <units/dimensions>, <= <triangles>, textures <= <pixels> px.
Exclude all other objects, including floor, camera, and lights. If selection is
empty or ambiguous, stop and ask; never fall back to exporting the whole scene.
Preserve all live objects and the editable source. Use a new saved/export copy for
conversion, baking, or modifier application; never delete or clear the live scene.
Confirm copy path <asset/source/export-v01.blend>, destination
<asset/exports/name-v01.glb>, and explicit overwrite permission for existing files.
After approval, export selected objects only. Verify the file exists and reimport
it into a separate disposable scene or inspect it in the target engine.
Done: report included objects, scale/orientation, materials/textures, budget,
destination, and checks actually performed. Flag unverified checks; file existence
alone is not success. Stop before any upload or publishing action.
```

For format details and engine loading, continue to [exporting](exporting.md).
