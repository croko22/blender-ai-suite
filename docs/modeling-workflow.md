# Build an asset you can reuse

Work in small visual steps: brief, blockout, previews, refinement, then export.
Start with a [reference brief](reference-to-prompt.md) and a suitable
[prompt template](prompt-library.md). Apply the [best practices](best-practices.md).

## 1. Describe the result

Name the object, intended style, target engine, dimensions/units, triangle and
texture budgets, and what must remain untouched. Mark unknowns for confirmation.
Inspect the scene and confirm a new saved working copy before edits; preserve
the original. Confirm each destination and whether an existing file may be overwritten.

> Add a stylized green pear next to the apple. Keep the apple, floor, and lights.
> Make the pear and stem separate named objects. I will export it for a web scene.

## 2. Approve the blockout

Inspect the silhouette from several angles before adding surface detail. Check
that the object sits on the floor, its parts meet, and adjacent objects do not
overlap accidentally. Compare a reference-matched view plus side and rear views;
the latter reveal assumptions, not evidence of hidden geometry. Stop for approval
of proportions and scale before surface detail. Keep edits in a named asset collection.

## 3. Add materials

Set colors on shader inputs, not only viewport display colors. Inspect the model
in Material Preview or Rendered shading. Keep materials simple for portability;
plan to bake procedural detail when exporting it.

## 4. Preview and revise one thing

Use a floor and a small lighting setup to judge the result. Check the camera
framing so the whole asset is visible. Treat this presentation scene separately
from the reusable model: a floor and studio lights need not ship with each fruit.
Keep camera and lighting fixed when judging a material change. Request one
measurable revision at a time, compare before/after previews, and approve or revert
that revision before the next. Preserve existing scene objects; never clear the live scene.

## 5. Save and verify

- Save the editable scene under the asset's `source/` folder.
- Keep a preview image beside it so the intended appearance is clear.
- Export a copy; keep the source scene editable.
- Reimport the export into a separate disposable scene or inspect it in the target
  engine; leave the working scene intact.
- Check scale, orientation, materials, missing textures, and object separation.

Next: [export for your target engine](exporting.md).
