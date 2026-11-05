# Turn a reference image into a bounded prompt

Describe what is visible, label what is uncertain, then approve a blockout before
detail. One image cannot establish exact unseen geometry or real-world scale.

## 1. Check rights and purpose

Use an image you own or have permission to use for this purpose. Record its source,
creator, license/permission, and attribution requirements. Permission to view an
image is not permission to redistribute it or copy protected designs. If rights
are unclear, ask for a cleared reference; do not bundle or upload it elsewhere.
Agree on the target engine, intended viewing distance, dimensions/units, triangle
budget, and maximum texture resolution before modeling.

## 2. Write an observable visual brief

| Field | Example: stylized watering can |
| --- | --- |
| Observed | Rounded body, narrow spout rising to the right, arched handle, matte green surface |
| Image-space proportions | Body roughly twice as wide as tall; spout tip near handle height |
| Uncertain | Rear handle attachment, wall thickness, underside, actual dimensions |
| Proposed assumptions | Closed decorative prop; simplified hidden surfaces; width 0.3 m, pending approval |
| Preserve | Existing scene, camera, lights, unrelated materials, and original source file |
| Acceptance | Recognizable silhouette in the reference view; plausible side/rear views; agreed size and budget |

Image ratios are estimates, not calibrated dimensions: perspective, shadows, and
occlusion can mislead. Request more views or one known measurement when accuracy
matters. If unavailable, agree on an approximation rather than claiming a reconstruction.

## 3. Convert the brief into a staged request

Fill the [reference-prop template](prompt-library.md#reference-based-prop) with
the observed features, approved assumptions, constraints, and destination. Ask
for scene inspection and a plan first, then a simple blockout. Proceed only when
the user approves its dimensions and silhouette in a preview.

## 4. Compare and revise

Match the reference's camera angle approximately, then inspect side and rear views
for implausible joins or intersections. Name the difference, not just the feeling:
“Reduce body width by 10%; keep height, spout, camera, and lighting unchanged.”
Approve shape before materials; use [material/lighting iteration](prompt-library.md#material-and-lighting-iteration)
for appearance. Finish with the [modeling and export checks](modeling-workflow.md#5-save-and-verify).
