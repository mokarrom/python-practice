"""In windows, src directory is not in sys.path or PYTHONPATH. Therefore, the following code snippet will add it.
This file will run before collecting any test. It will also add the current directory into sys.path."""
import os
import sys
from pathlib import Path

SRC_DIR = os.path.join(Path(__file__).parent.parent, "src")

sys.path.insert(1, SRC_DIR)

