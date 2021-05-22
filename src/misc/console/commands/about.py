"""Command subclass defining the CLI's about command."""
from cleo import Command
from misc.console.commands.return_codes import RETURN_CODES


class AboutCommand(Command):
    """Learn about the misc CLI."""

    name = "about"

    def handle(self):
        """The about command routine."""
        self.line("""misc CLI\nPython Practice Code""")
        return RETURN_CODES.success.value
