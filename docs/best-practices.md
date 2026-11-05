# Keep Blender iterations safe and useful

Use this checklist alongside the [modeling workflow](modeling-workflow.md).
The [prompt library](prompt-library.md) turns these constraints into bounded requests.

## Before an edit

- Inspect the actual connected scene; name the objects allowed to change and what
  must remain untouched. A connected tool is not proof of the correct Blender window.
- Save a new versioned working copy; retain the original. Confirm destination and
  overwrite permission before every save, preview write, bake, or export.
- Keep changes additive and scoped to a named collection. Never clear or delete
  the live scene to make a recipe work; ask when an object or prerequisite is missing.
- Agree on engine, units/dimensions, viewing distance, triangle budget, and texture
  resolution. Measure the evaluated/export geometry, not just the low-resolution cage.
- Check reference rights and label uncertain geometry in the [visual brief](reference-to-prompt.md).

## During iteration

- Approve silhouette and scale before detail. Check joins, floor contact, and
  intersections from multiple angles; a good hero view can hide broken geometry.
- Change one variable per preview comparison. Keep camera, lighting, and color
  management fixed for material comparisons; record settings that changed.
- Check shader colors in Material Preview or Rendered shading, not Solid alone.
  Duplicate shared materials before scoped edits that would affect other objects.
- Keep modifiers editable in the source; convert or apply them on export copies.
  Separate the reusable asset from presentation floors, cameras, and studio lights.

## Before delivery

- Save external images and check portable texture paths. Bake procedural detail
  only when needed for the target; keep studio lighting out of relightable base color.
- Verify the explicit export set includes all asset parts and excludes unrelated
  scene objects. An empty selection is a reason to stop, not export everything.
- Inspect the exported result in a separate scene or target engine for scale,
  orientation, hierarchy, materials, textures, and budget. File existence is insufficient.
- Record reference/asset provenance, checked results, and remaining unknowns with
  the asset using the [folder conventions](../assets/README.md). Report unperformed
  checks honestly; upload or publication requires separate approval.

See [exporting](exporting.md) for format-specific guidance and the
[skill audit](skill-audit.md) for imported recipe verification limits.
