"""Create and configure the CLI application and its commands."""
from cleo import Application
from misc import __version__
from misc.console.commands import AboutCommand


def generate_application() -> Application:
    """Create, configure, and run the CLI application."""
    application = Application("misc", __version__)
    application.add(AboutCommand())
    return application


def main() -> None:  # pragma: no cover
    """Main function used as CLI entry point. Configured as script in pyproject.toml."""
    app = generate_application()
    app.run()


if __name__ == "__main__":
    main()
