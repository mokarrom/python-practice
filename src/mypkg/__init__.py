"""Package initialization."""
__version__ = "0.1.0"
__title__ = "mypkg"
__description__ = "My Python  Package"
__doc__ = __description__
__author__ = ""
__email__ = ""
__pdoc__ = {"scripts": False}

import logging

from mypkg.logger import MyPkgLogger

logging.setLoggerClass(MyPkgLogger)
