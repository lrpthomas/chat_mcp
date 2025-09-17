# ChatGPT Desktop MCP Configuration

This directory contains configuration files for integrating the chat_mcp server with ChatGPT Desktop.

## Configuration Files

### claude_desktop_config.json
Example configuration for Claude Desktop (similar format used by ChatGPT Desktop):

```json
{
  "mcpServers": {
    "chat-mcp": {
      "command": "uv",
      "args": ["run", "chat-mcp"],
      "cwd": "/path/to/your/chat_mcp"
    }
  }
}
```

### Alternative configurations

#### Using Python directly:
```json
{
  "mcpServers": {
    "chat-mcp": {
      "command": "python",
      "args": ["-m", "chat_mcp.server"],
      "cwd": "/path/to/your/chat_mcp"
    }
  }
}
```

#### Using pip installed package:
```json
{
  "mcpServers": {
    "chat-mcp": {
      "command": "chat-mcp"
    }
  }
}
```

## Setup Instructions

1. Install the package:
   ```bash
   pip install -e .
   ```

2. Add the configuration to your ChatGPT Desktop settings

3. Restart ChatGPT Desktop

4. The chat-mcp tools should now be available in your chat interface