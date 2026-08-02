from fastmcp import FastMCP

mcp = FastMCP("Google Sheets")

@mcp.tool()
def hello():
    return "Hello from Google Sheets."

app = mcp.http_app()
