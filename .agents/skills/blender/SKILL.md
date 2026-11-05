---
name: Blender
description: "Control Blender from the shell via Flue - a Python bridge to bpy without an MCP server."
license: MIT
---
This skill lets a coding agent operate **Blender** on the desktop through [Flue](https://github.com/SFKislev/flue), a local shell-to-application bridge. The agent pipes Python into `blender_bridge.py` and gets structured JSON back. Flue is **not an MCP server** — it is a thinner, simpler shell contract that drives Blender's own `bpy` runtime directly.

> agent shell -> `blender_bridge.py` -> bpy -> JSON result

## When to use
The human requests work performed **inside Blender** — inspect the open scene, collections, objects, meshes, materials, selection; make bounded edits; run small `bpy` scripts. A CLI agent needs an application automation interface, such as connected MCP tools or Flue; Flue is not required when MCP already provides the needed capability.

## How to proceed
1. Read [the shared runtime contract](../BLENDER_RUNTIME.md) before any Blender call. Discover available capabilities and perform read-only connectivity checks.
2. **For the optional Flue branch:** read [FLUE.md](FLUE.md), then locate the installed Flue skill and its `adapters/blender_adapter/APP.md` through host discovery or a user-provided installation directory. Do not assume an author's filesystem path or bridge arguments.
3. **If Flue is requested but unavailable:** report that branch unavailable. Installation/setup requires explicit approval in the current session; an existing MCP connection does not require Flue installation.

## Other apps
Flue also supports Photoshop, Illustrator, Premiere, After Effects, InDesign, Audition, Houdini, 3ds Max, Unity, and Microsoft Office through the same stdin/stdout contract. One install covers all adapters.

## Safety
Flue acts inside professional desktop software. Treat the human as the driver; prefer small, inspectable steps; avoid destructive actions unless explicitly requested. Flue is MIT-licensed and reviewable on GitHub / PyPI before use.
