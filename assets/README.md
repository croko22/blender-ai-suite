# Asset organization

Keep each asset's editable source, dependencies, preview, and exports together.
No model files are bundled yet.

## Suggested layout

```text
assets/
  apple/
    source/         # Editable .blend files
    textures/       # Saved image textures
    previews/       # Small images showing the intended result
    exports/        # GLB or other engine-ready deliveries
```

Use descriptive lowercase names. Keep texture paths portable and check for
missing external files before sharing a `.blend` source. Save a short note with
each asset explaining its origin, license, intended scale, and export checks.

Commit small, intentional assets only. For large binaries, plan Git LFS before
adding them; merely deleting a committed file does not remove it from Git history.
Blender backup files and temporary render folders are ignored by default.
