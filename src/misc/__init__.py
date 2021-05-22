"""Top-level package for misc."""
try:
    # Use python core import metadata when ≥ 3.8
    from importlib import metadata  # type: ignore
    from importlib.metadata import PackageNotFoundError
except ImportError:
    # Use third party import_metadata
    import importlib_metadata as metadata  # type: ignore
    from importlib_metadata import PackageNotFoundError  # type: ignore

__all__ = ["__version__"]

# Determine the package version from the package settings
# https://packaging.python.org/guides/single-sourcing-package-version/
__version__ = "DEV"  # If running outside of a package (developing) it may not be set
try:
    __version__ = metadata.version(__name__)
except PackageNotFoundError:
    pass
