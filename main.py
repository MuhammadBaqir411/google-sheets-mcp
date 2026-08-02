from fastmcp import FastMCP

mcp = FastMCP("Google Sheets")

@mcp.tool()
def hello():
    return "Google Sheets MCP server is running."

if __name__ == "__main__":
    mcp.run()
