# Prompts Book MCP Server Guide
### *Autonomous Tool Integration for Claude Desktop, Cursor & Antigravity*
**Architect:** **Muhammad Nasir Khan**

The **Prompts Book MCP Server** exposes Muhammad Nasir Khan's prompt compilation, quality linting, and audio-visual synchronization engines directly as callable tools for AI agents.

---

## 🛠️ Available MCP Tools

1. `generate_video_prompt`: Compiles production-ready video prompts using the 5-layer **MCSLA Framework** (Model, Camera, Subject, Look, Action/Audio).
2. `generate_audio_prompt`: Compiles Suno AI style-box prompts (with character audits) using the **7-Element Audio Formula**.
3. `calculate_bpm_sync`: Calculates exact frame cut intervals at 24fps, 30fps, or 60fps locked mathematically to any musical BPM.

---

## 🔌 Connecting to Claude Desktop / Cursor / Antigravity

Add the following block to your `claude_desktop_config.json` or your agent MCP configuration:

```json
{
  "mcpServers": {
    "prompts-book": {
      "command": "python",
      "args": [
        "E:/AI PROJECTS/Prompts Book/tools-and-workflows/mcp-server/server.py"
      ]
    }
  }
}
```

---

## 💡 Example Agent Tool Invocations

### 1. Generating a Cinematic Video Prompt:
```json
{
  "name": "generate_video_prompt",
  "arguments": {
    "subject": "A cybernetic courier with a neon visor",
    "environment": "Rain-slicked alley in dystopian Neo-Tokyo",
    "action": "Ducks under a falling metal sign and activates wrist holoscreen",
    "camera_preset": "Action Run low angle tracking 1m behind him",
    "engine": "Kling 3.0",
    "aspect": "16:9",
    "duration": "8s",
    "lighting": "Cyan and magenta neon specular reflections, wet asphalt"
  }
}
```

### 2. Audio-to-Video BPM Synchronization:
```json
{
  "name": "calculate_bpm_sync",
  "arguments": {
    "bpm": 124,
    "fps": 30
  }
}
```
*Output: Exactly 14.5 frames per beat, 58 frames per 4-beat bar.*
