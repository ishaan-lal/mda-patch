from managed_deepagents import connections, define_mcp

mcp = define_mcp(
    servers={
        "github": {
            "transport": "http",
            "url": "https://api.githubcopilot.com/mcp/",
            "connection": connections.get("patch-github", {"type": "user"}),
            "include_tools": [
                "get_file_contents",
                "create_branch",
                "create_or_update_file",
                "push_files",
                "create_pull_request",
            ],
        },
    },
    throw_on_load_error=False,
)
