# Imported skill index

This directory is a human index, not an install destination. The five canonical
imports live under `.agents/skills/`; `.claude/skills/` contains relative symlinks
to the same directories. Follow your client's discovery and activation rules:
neither layout guarantees automatic loading in every client.

| Skill | Use | Connection |
| --- | --- | --- |
| [blender](../.agents/skills/blender/SKILL.md) | General scene inspection and bounded edits | Optional Flue shell bridge |
| [blender-modeling](../.agents/skills/blender-modeling/SKILL.md) | Geometry and modifiers | Runtime-discovered Blender MCP |
| [blender-animation](../.agents/skills/blender-animation/SKILL.md) | Keyframes and motion | Runtime-discovered Blender MCP |
| [blender-rendering](../.agents/skills/blender-rendering/SKILL.md) | Lighting, cameras, and renders | Runtime-discovered Blender MCP |
| [blender-export](../.agents/skills/blender-export/SKILL.md) | Export preparation and delivery | Runtime-discovered Blender MCP |

Flue and MCP are separate routes, not two mandatory components. Flue is not an
MCP server and is not required for the four MCP skills. Discover the available
tools at runtime rather than assuming a recipe's tool names exist in your client.
Dedicated materials, wireframe, and reference-calibration skills are not imported.

See [connection setup](../docs/getting-started.md), the
[audit and verification limits](../docs/skill-audit.md), and
[third-party notices](../THIRD_PARTY_NOTICES.md).
[skills-lock.json](../skills-lock.json) records imported provenance; local fixes
are not guaranteed to match upstream hashes.

## Before importing

- Check the original license and retain required attribution.
- Read the instructions and any scripts before enabling execution.
- Keep each skill focused on one job and list its prerequisites.
- Explain which scene objects or files it may change.
- Include a small example and an observable way to check success.
- Record the source URL and imported version or revision for future updates.

After importing, update this index with a link, purpose, and connection requirement.
