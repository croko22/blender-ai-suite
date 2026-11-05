# Build an asset you can reuse

Work in small visual steps: shape, materials, presentation, then export.

## 1. Describe the result

Name the object, intended style, target engine, and what must remain untouched.

> Add a stylized green pear next to the apple. Keep the apple, floor, and lights.
> Make the pear and stem separate named objects. I will export it for a web scene.

## 2. Check the shape

Inspect the silhouette from several angles before adding surface detail. Check
that the object sits on the floor, its parts meet, and adjacent objects do not
overlap accidentally. Use a triangle budget appropriate to the target project.

## 3. Add materials

Set colors on shader inputs, not only viewport display colors. Inspect the model
in Material Preview or Rendered shading. Keep materials simple for portability;
plan to bake procedural detail when exporting it.

## 4. Add presentation

Use a floor and a small lighting setup to judge the result. Check the camera
framing so the whole asset is visible. Treat this presentation scene separately
from the reusable model: a floor and studio lights need not ship with each fruit.

## 5. Save and verify

- Save the editable scene under the asset's `source/` folder.
- Keep a preview image beside it so the intended appearance is clear.
- Export a copy; keep the source scene editable.
- Reimport the export into a fresh scene or inspect it in the target engine.
- Check scale, orientation, materials, missing textures, and object separation.

Next: [export for your target engine](exporting.md).
