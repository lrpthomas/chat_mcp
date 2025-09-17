# ChatGPT Desktop MCP Server

A Model Context Protocol (MCP) server implementation designed for integration with ChatGPT Desktop.

## Overview

This project provides an MCP server that can be integrated with ChatGPT Desktop to extend its capabilities with custom tools and resources. The server implements the MCP specification and provides a foundation for building chat-related functionality.

## Features

- **Echo Tool**: Simple text echoing functionality for testing
- **Time Tool**: Get current timestamp
- **Status Tool**: Check server status
- **Resource Access**: Access server information and status via MCP resources
- **Async Support**: Full async/await support for scalable operations

## Installation

### Using pip (recommended)

```bash
pip install -e .
```

### Using uv (faster)

```bash
uv install
```

## Configuration for ChatGPT Desktop

1. Copy the configuration from `config/claude_desktop_config.json`
2. Add it to your ChatGPT Desktop MCP settings
3. Update the `cwd` path to point to your installation directory
4. Restart ChatGPT Desktop

Example configuration:
```json
{
  "mcpServers": {
    "chat-mcp": {
      "command": "chat-mcp",
      "cwd": "/path/to/your/chat_mcp"
    }
  }
}
```

## Usage

### Running the server directly

```bash
# Using the installed command
chat-mcp

# Or using Python module
python -m chat_mcp.server
```

### Available Tools

1. **echo**: Echo back input text
2. **get_time**: Get current timestamp  
3. **chat_status**: Get server status

### Available Resources

1. **chat://status**: Server operational status
2. **chat://info**: Server information and capabilities

## Development

### Setup development environment

```bash
pip install -e ".[dev]"
```

### Running tests

```bash
pytest
```

### Code formatting

```bash
black src/
ruff check src/
```

### Type checking

```bash
mypy src/
```

## Project Structure

```
chat_mcp/
├── src/chat_mcp/          # Main package
│   ├── __init__.py        # Package initialization
│   └── server.py          # MCP server implementation
├── config/                # Configuration examples
│   ├── claude_desktop_config.json
│   └── README.md
├── tests/                 # Test suite
├── pyproject.toml         # Project configuration
└── README.md             # This file
```

## License

MIT License
