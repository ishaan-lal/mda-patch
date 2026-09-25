from managed_deepagents import channels

channel = channels.slack(
    name="Patch-agent",
    description="Fixes bugs and implements small features, \
    then opens a pull request.",
)
