#!/usr/bin/env python3
"""
ChatGPT Desktop MCP Server

A basic MCP server implementation that provides chat-related tools and resources
for integration with ChatGPT Desktop.
"""

import logging
import asyncio
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    CallToolRequest,
    ListResourcesRequest,
    ListToolsRequest,
    ReadResourceRequest,
)
from pydantic import BaseModel


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChatMCPServer:
    """Main MCP server class for ChatGPT Desktop integration."""
    
    def __init__(self) -> None:
        self.server = Server("chat-mcp")
        self._setup_handlers()
    
    def _setup_handlers(self) -> None:
        """Set up MCP protocol handlers."""
        
        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            """List available tools."""
            return [
                Tool(
                    name="echo",
                    description="Echo back the input text",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string",
                                "description": "Text to echo back"
                            }
                        },
                        "required": ["text"]
                    }
                ),
                Tool(
                    name="get_time",
                    description="Get the current time",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                ),
                Tool(
                    name="chat_status",
                    description="Get chat server status",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                )
            ]
        
        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            """Handle tool calls."""
            if name == "echo":
                text = arguments.get("text", "")
                return [TextContent(type="text", text=f"Echo: {text}")]
            
            elif name == "get_time":
                import datetime
                current_time = datetime.datetime.now().isoformat()
                return [TextContent(type="text", text=f"Current time: {current_time}")]
            
            elif name == "chat_status":
                return [TextContent(
                    type="text", 
                    text="ChatGPT Desktop MCP Server is running and ready for connections"
                )]
            
            else:
                raise ValueError(f"Unknown tool: {name}")
        
        @self.server.list_resources()
        async def handle_list_resources() -> List[Resource]:
            """List available resources."""
            return [
                Resource(
                    uri="chat://status",
                    name="Server Status",
                    description="Current status of the chat MCP server",
                    mimeType="text/plain"
                ),
                Resource(
                    uri="chat://info",
                    name="Server Information", 
                    description="Information about the chat MCP server",
                    mimeType="application/json"
                )
            ]
        
        @self.server.read_resource()
        async def handle_read_resource(uri: str) -> str:
            """Read resource content."""
            if uri == "chat://status":
                return "ChatGPT Desktop MCP Server is operational"
            
            elif uri == "chat://info":
                import json
                info = {
                    "name": "ChatGPT Desktop MCP Server",
                    "version": "0.1.0",
                    "description": "MCP server for ChatGPT Desktop integration",
                    "tools": ["echo", "get_time", "chat_status"],
                    "resources": ["chat://status", "chat://info"]
                }
                return json.dumps(info, indent=2)
            
            else:
                raise ValueError(f"Unknown resource: {uri}")
    
    async def run(self) -> None:
        """Run the MCP server."""
        logger.info("Starting ChatGPT Desktop MCP Server...")
        
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream, 
                write_stream,
                InitializationOptions(
                    server_name="chat-mcp",
                    server_version="0.1.0",
                    capabilities={
                        "tools": {},
                        "resources": {}
                    }
                )
            )


def main() -> None:
    """Main entry point."""
    async def _main() -> None:
        server = ChatMCPServer()
        await server.run()
    
    asyncio.run(_main())


if __name__ == "__main__":
    main()