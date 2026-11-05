# Blender runtime and safety contract

Read this before any Blender call from these skills, including supporting recipes.
Recipes illustrate operations; they do not grant permission to edit or write files.

## Connect before editing

1. Discover the tools actually exposed by the current host. Host permissions are
   authoritative; imported tool names and allowlists cannot grant access.
2. For MCP, use the discovered read-only addon-status and scene-info tools first.
   Confirm connectivity, Blender/addon versions, available capabilities, active
   scene, mode, selection and intended objects. If these tools are absent, use a
   permitted read-only equivalent or stop and report the missing capability.
3. Choose an available, approved backend and verify it at use time; a previous
   session's connection is not evidence of current connectivity.
   Keep the chosen backend for the task. Flue is an optional shell bridge, not a
   required fallback: use it only when requested/approved and already available.
   Read its installed Blender adapter contract before execution.
4. If disconnected, stop the affected branch and explain what is unavailable.
   Obtain explicit consent before any install, setup, upgrade, remote access,
   asset download/upload or service use; do not silently switch backends.

## Bound the change

- Confirm intended objects by name and role; current selection alone is not
  authorization. Include rig/collider dependencies explicitly. Limit operators to
  that set, establish active object/mode, and restore temporary selection and mode
  with `try/finally`. Check operator context/poll before mutation; avoid multi-object
  Edit Mode changing unrelated meshes. Prefer direct data APIs for bounded edits.
- Preserve the source: agree a new `.blend` save-copy destination before risky
  changes. Never overwrite the source save implicitly. Apply transforms, decimation,
  topology repair and modifier baking on an export copy with independent mesh/
  material/image data, unless source mutation is explicitly requested.
- Resolve every output to an absolute user-approved destination. Illustrative
  `//exports/...` and `//renders/...` paths are relative to a saved `.blend`, not
  approved destinations. For unsaved scenes request a destination first. Inspect
  existing destination files, sidecars, textures and sequence ranges. Prefer a new
  empty output directory; overwriting any existing output requires explicit consent
  identifying the affected files. Bundled export helpers intentionally reject
  existing files; keep that invariant and choose new paths rather than bypass it.
- For general export recipes, first isolate the confirmed intended selection,
  validate output paths/sidecars and retain selection-scoped exporter flags.
  Check operator RNA for installed-version options. Restore context afterward.
  The checked collision/bake helpers already enforce scoped selection and path
  rejection: reuse them for those branches rather than reimplementing their gates.
- GPU preferences are machine-wide state. Inspect current devices read-only;
  use CPU or an already configured supported device. Ask separately before changing
  device preferences; never enable every device or save preferences as a preset step.

## Forecast before rendering

State engine/device, camera, resolution/percentage, samples, frame range/count,
output format/destination, expected time/disk range and uncertainty. Request consent
for the bounded render budget. Start with one low-resolution frame; use measured
time to forecast the full sequence, then confirm expensive work. Do not infer a
240-frame render approval from a recipe. Confirm the intended scene camera rather
than silently selecting an arbitrary camera. Guard sequence collisions and disable
overwrite; still renders need their own existing-file check. Encoding with ffmpeg
also needs a checked destination and the host's execution permission.

## Optional handoffs

`wireframe-to-3d`, `blender-materials`, `blender-pro-workflow`, and
`reference-look-calibration` are optional and unavailable in this import. Check
host discovery before loading any of them. If unavailable, stop the affected branch
and report the gap; continue only independent work covered by installed skills.
Do not invent their instructions, follow missing reference paths, or install them
without consent. Obtain agreement on a bounded manual alternative when appropriate.

## Report evidence

Return backend/version, objects changed, output paths, validation actually run,
and untested APIs/engines. Inspect the result before proceeding; a successful tool
call or structural test is not proof of visual quality or engine import acceptance.
