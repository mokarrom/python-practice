"""Tests for `misc` package."""


import pytest
from cleo import CommandTester
from os import system

from misc.console import application  # noqa: F401


@pytest.fixture
def class_import():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    from src import misc
    from src.misc import console  # noqa: F401
    from src.misc.console import application, commands  # noqa: F401,F811
    from src.misc.console.commands import return_codes  # noqa: F401,F811

    return misc


def test_class_import_initialization(class_import):
    assert hasattr(class_import, "__version__")
    assert hasattr(class_import, "console")
    assert hasattr(class_import.console, "commands")
    assert hasattr(class_import.console, "application")


def test_console_command(class_import):
    application = class_import.console.application.generate_application()  # noqa: F811

    command = application.find("about")
    command_tester = CommandTester(command)
    command_tester.execute()
    assert """misc CLI\nPython Practice Code\n""" == command_tester.io.fetch_output()


def test_command_line_execution(class_import):
    RETURN_CODES = class_import.console.commands.return_codes.RETURN_CODES
    assert RETURN_CODES.success.value == int(system("python src/misc/console/application.py about"))
