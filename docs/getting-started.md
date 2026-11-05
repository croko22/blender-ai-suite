# Connect Blender and your AI assistant

The first goal is simple: your assistant can read the scene that is open in Blender.

## Before you start

- Install Blender and save a working `.blend` file.
- Use an AI client with Blender MCP tools configured.
- Install the Blender addon required by that particular MCP server.

MCP integrations differ. Use the installation instructions for your chosen
integration, and keep its server and addon versions compatible. This repository
does not install or configure either component.

## Check the connection

1. Open Blender and enable your MCP addon.
2. Start its server inside Blender if the addon requires that step.
3. Connect your AI client to the configured MCP server.
4. Ask the assistant to read the addon status and list scene objects.
5. Confirm that the returned objects match the window you are using.

An MCP tool appearing in your client does **not** prove that it can reach Blender.
Check the actual tool response before asking it to change the scene.

## First request

> Inspect the current scene, then add a red apple with a stem and leaf. Preserve
> existing objects. Use readable object names and show me the result.

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

Next: [model an asset](modeling-workflow.md).
