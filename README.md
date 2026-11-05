# Blender AI Suite

**From a prompt to a reusable 3D asset.**

A personal workshop for learning Blender with AI, collecting reusable skills,
and taking models into Three.js, Roblox, and other development projects.

This repository starts with documentation and a place to import skills.
It is not a Blender addon, an installed skill pack, or an automated export tool.

## Start here

1. [Connect Blender to your AI tools](docs/getting-started.md).
2. [Follow the modeling workflow](docs/modeling-workflow.md).
3. [Export assets for Three.js or Roblox](docs/exporting.md).
4. [Import your own skills](skills/README.md).

## Repository map

| Location | Purpose |
| --- | --- |
| [`docs/`](docs/README.md) | Setup, modeling, and export guides |
| [`skills/`](skills/README.md) | Reusable skills you import later |
| [`assets/`](assets/README.md) | Blender sources, textures, previews, and exports |

## First exercise: a fruit scene

Create an apple and a pear, give them materials, and add a floor and lighting.
Then export each fruit independently and check it in the target engine.

Keep a `.blend` source file: a portable export is a delivery artifact, not a
replacement for the editable scene.

> Procedural Blender materials do not automatically survive export. Bake their
> appearance into image textures when you need it in another engine.

## Current scope

- Included: starter documentation and folder conventions.
- Next: import and review your skills, then add tested example assets.
- Not included yet: skill implementations, models, scripts, or a demo app.

## Sharing

No license has been selected yet. Public visibility does not grant an open-source
license. Record the source and license of third-party skills and assets before
adding or redistributing them.
