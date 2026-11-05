# Connect Blender and your AI assistant

The first goal is simple: your assistant can read the scene that is open in Blender.

## Before you start

- Install Blender and save a working `.blend` file.
- For the four MCP skills, use an AI client with Blender MCP tools configured and
  the Blender addon required by that server.
- Alternatively, the optional `blender` skill uses the Flue shell bridge. Read
  its prerequisites in the [skill index](../skills/README.md); it is not MCP.

MCP integrations differ. Use the installation instructions for your chosen
integration, and keep its server and addon versions compatible. This repository
does not install or configure either component.
Choose the route your client supports; you do not need both backends.

## Check the MCP connection

1. Open Blender and enable your MCP addon.
2. Start its server inside Blender if the addon requires that step.
3. Connect your AI client to the configured MCP server.
4. Discover available tools, then ask the assistant to read addon status (if
   supported) and list scene objects using that backend's read-only tools.
5. Confirm that the returned objects match the window you are using.

An MCP tool appearing in your client does **not** prove that it can reach Blender.
Check the actual tool response before asking it to change the scene.
For Flue, follow its bridge instructions and perform the same read-only object
check before editing. Skill discovery is client-specific, not automatic everywhere.

## First request

> Inspect the current scene and propose a red apple blockout with a stem and leaf.
> Preserve all existing objects. Ask me to confirm dimensions, target budget, and
> a new working-copy save path before editing. Show a preview before detailing.

Switch the viewport to Material Preview or Rendered shading to inspect materials.
Solid shading alone is not a reliable preview of shader colors.

## If the connection fails

Check that Blender is open, the addon is enabled, its server is started, and the
client is configured for the same endpoint. Then repeat the read-only scene check.
Do not replace or clear the scene to troubleshoot a connection problem.

## Keep control of your scene

- Save before running generated code; review scripts from untrusted sources.
- Ask for additive edits rather than deleting existing objects.
- Keep the MCP endpoint local unless you deliberately configure secure remote access.
- Confirm the destination before uploading assets or publishing repository content.

Next: [write a reference brief](reference-to-prompt.md), then
[model an asset](modeling-workflow.md).
