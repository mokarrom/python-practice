"""Module for any logging-related capabilities."""
import sys
import logging
from logging import Logger
from logging.handlers import TimedRotatingFileHandler


class MyPkgLogger(Logger):
    """Handles logging to the console and a file as well.

    Based on code in this gist: https://gist.github.com/nguyenkims/e92df0f8bd49973f0c94bddf36ed7fd0
    """

    # pylint: disable=keyword-arg-before-vararg
    def __init__(self, *args, **kwargs):
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.log_file = "issue-level.log"

        Logger.__init__(self, *args, **kwargs)

        self.addHandler(self.get_console_handler())
        self.addHandler(self.get_file_handler())

        self.propagate = False

    def get_console_handler(self):
        """Gets a logging handler that writes to the console output."""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def get_file_handler(self):
        """Gets a logging handler that writes to a file."""
        file_handler = TimedRotatingFileHandler(self.log_file, when="midnight")
        file_handler.setFormatter(self.formatter)
        return file_handler
