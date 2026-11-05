# Blender AI Suite

**From a prompt to a reusable 3D asset.**

A personal workshop for learning Blender with AI, collecting reusable skills,
and taking models into Three.js, Roblox, and other development projects.

This repository contains workflow guides, prompt templates, and five imported
agent skills. It is not a Blender addon or an automated export tool; skill
activation and a working Blender connection depend on your AI client.

## Start here

1. [Connect Blender to your AI tools](docs/getting-started.md).
2. [Turn a reference into a visual brief](docs/reference-to-prompt.md).
3. [Follow the modeling workflow](docs/modeling-workflow.md) using the
   [copy-paste prompts](docs/prompt-library.md).
4. [Export assets for Three.js or Roblox](docs/exporting.md).

Keep the [best-practices checklist](docs/best-practices.md) nearby; browse the
[skill index](skills/README.md) when choosing a capability.

## Repository map

| Location | Purpose |
| --- | --- |
| [`docs/`](docs/README.md) | Setup, modeling, and export guides |
| [Skill index](skills/README.md) | Human navigation; canonical skills live in `.agents/skills/` |
| [`assets/`](assets/README.md) | Conventions for future Blender sources, textures, previews, and exports |

## First exercise: a fruit scene

Create an apple and a pear, give them materials, and add a floor and lighting.
Then export each fruit independently and check it in the target engine.

Keep a `.blend` source file: a portable export is a delivery artifact, not a
replacement for the editable scene.

> Procedural Blender materials do not automatically survive export. Bake their
> appearance into image textures when you need it in another engine.

## Current scope

- Included: five imported skills with their support files, guides, and prompt templates.
- Prompt templates are examples, not tested generated assets or runtime guarantees.
- No models, generated scene examples, standalone project scripts, or demo app are bundled.
- See the [skill audit](docs/skill-audit.md) for corrections and verification limits.

## Sharing

No license has been selected yet. Public visibility does not grant an open-source
license. Record the source and license of third-party skills and assets before
adding or redistributing them. Imported skill notices are in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); those notices do not select a
license for the repository as a whole.
