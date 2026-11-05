# Export Blender assets for development

Keep `.blend` files as editable sources. Start with `.glb` for a portable asset;
use another format when your target project's importer requires it.

## Prepare the model

1. Save the source scene before changing anything for export.
2. Select the asset and all its parts, such as the fruit, stem, and leaf.
3. Check scale, orientation, origin, and modifier results on an export copy.
4. Convert curve-based parts to meshes on that copy if the exporter needs meshes.
5. Inspect the resulting triangle count; subdivision can increase it significantly.

Export the apple and pear separately if you want independent reusable props.
Leave the floor, camera, and lights out unless you intentionally need them.

## Preserve materials

Blender's procedural noise, ramps, and custom shader graphs are not portable
shader programs. The glTF exporter recognizes supported material arrangements;
it does not reproduce arbitrary Blender node graphs.

For procedural assets:

1. UV unwrap the meshes.
2. Bake the required surface detail into image textures, such as base color.
3. Save the baked images and connect them to export-compatible materials.
4. Use Non-Color data for roughness, metallic, and normal maps.
5. Inspect a test export before calling the asset finished.

Do not bake studio lighting into base color if the asset should be relit in-game.
For glTF, packed roughness uses the green channel and metallic uses the blue.

## Export a GLB

In Blender, choose **File → Export → glTF 2.0**, select the binary `.glb` format,
and enable **Selected Objects**. Save under the asset's `exports/` folder.

GLB can package mesh data and image textures in one file. Blender area lights do
not export through glTF's punctual-light extension; set up lighting in your engine.

## Three.js

Place `apple.glb` in your app's public assets directory. In an existing Three.js
app with a configured `scene`, load it with `GLTFLoader`:

```js
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const loader = new GLTFLoader();

loader.load(
  '/models/apple.glb',
  (gltf) => scene.add(gltf.scene),
  undefined,
  (error) => console.error('Could not load apple:', error),
);
```

This is a loader snippet, not a complete application. Your app still needs its
renderer, camera, render loop, and lighting or an environment. Serve the asset
through the development server rather than opening an HTML file directly.

## Roblox Studio

Use Studio's **3D Importer** to select and preview the asset. Its documentation
includes `.gltf` / `.glb` support; `.fbx` is another option for projects using it.
Inspect scale, material appearance, hierarchy, and collision settings before use.
Importing or uploading assets to Roblox is a separate publishing action.

## Final check

- All intended parts are present, with no unintended scene objects.
- Scale and orientation work in the target project.
- Textures load and the materials remain recognizable under new lighting.
- Geometry and texture sizes fit the target project's performance budget.
- Collision behavior is appropriate for the asset's intended use.

## Official references

- [Blender glTF exporter](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html)
- [Three.js GLTFLoader](https://threejs.org/docs/#examples/en/loaders/GLTFLoader)
- [Roblox 3D Importer](https://create.roblox.com/docs/studio/importer)
