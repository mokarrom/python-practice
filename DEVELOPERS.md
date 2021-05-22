# Developing

*See [CONTRIBUTING](CONTRIBUTING.md) for how to contribute code if you are not already a primary developer of this repository.*

## Prerequisites

*You need...*

1. Python 3
2. `poetry`
3. A TR Artifactory API key

[See further prerequisite guidance](https://python.labs.thomsonreuters.com/get-started/prerequisites/)

## Development installation

**Clone this repository.**

```
$ git clone https://github.com/mokarrom/python-practice.git.git
```

**Install the package and its dependencies into a virtual environment.** Poetry automatically creates a virtual environment and installs all depdendencies into it.

```
cd python-practice
poetry install
```

A [.venv directory](https://python.labs.thomsonreuters.com/reference/#venv-directory) should now appear. This is where `poetry` installed your virtual environment.

**You can activate this virtual environment** anytime using either `poetry run` or `poetry shell`

```
poetry run python
```

```
poetry shell
python
```

**Install git hooks.** We use precommit checks to keep a variety of issues from making it into our shared codebases.

```
poetry run pre-commit install
```

You should now be able to execute the precommit check task. See *Coding standards* below.

[See further git hooks installation guidance](https://python.labs.thomsonreuters.com/get-started/install-git-hooks/)</br>

## Coding standards

**Use precommit checks** to enforce formatting, check for merge conflicts, private keys, proper docstrings, etc.

```
poetry run poe precommit-checks
```

[See further precommit check guidance](https://python.labs.thomsonreuters.com/get-started/install-git-hooks/)</br>
[See further `poe` task guidance](https://python.labs.thomsonreuters.com/reference/#poe)

**Also see other code standard configurations**...

- `.editorconfig` for general editor configuration.
- `.flake8` for coding style configurations.
- The `tool.black` section of `pyproject.toml` for further style configurations.
- `mypy.ini` for static type checking configuration.


## Configuring your IDE

[See further IDE configuration guidance](https://python.labs.thomsonreuters.com/get-started/configure-your-ide/)

Known Issues:

- If code coverage is enabled in pytest, it breaks the debugger
  - <https://youtrack.jetbrains.com/issue/PY-20186>
  - <https://github.com/pytest-dev/pytest-cov/issues/131>

## Testing

**Run all precommit checks and tests.**

```
poetry run poe test
```

**Or run just the tests.**

```
poetry run poe pytest
```

**NOTE**:

- Tests will fail if minimum coverage is not yet met.
- All tests are in the [`tests` directory](https://python.labs.thomsonreuters.com/reference/#tests-directory).
- All test reports are written to the [`htmlcov` directory](https://python.labs.thomsonreuters.com/reference/#htmlcov-directory).

[See further testing guidance](https://python.labs.thomsonreuters.com/testing/run-tests/)</br>
[See further `poe` task guidance](https://python.labs.thomsonreuters.com/reference/#poe)

## Documentation

**Build package documentation**.

```bash
poetry run poe build-docs
```

You can now view the package documentation by opening `python-practice/docs/misc/index.html` using your browser.

**Deploy package documentation locally**.

You can also host and review the package documentation on `localhost` (instead of manually pointing your browser to the build's `index.html` as suggested just above).

```bash
poetry run poe host-local-docs
```

[See further package documentation guidance](https://python.labs.thomsonreuters.com/documentation/build-docs/)</br>
[See further `poe` task guidance](https://python.labs.thomsonreuters.com/reference/#poe)

## Building and publishing

**Build package to wheel**

```
poetry run poe build-wheel
```

**You can also publish and/or release your package** using similar commands, if TR Artifactory has been setup to do so.

```
poetry run poe publish
```

```
poetry run poe release
```

[See further package publishing guidance](https://python.labs.thomsonreuters.com/publishing/publish-your-package/)</br>
[See further `poe` task guidance](https://python.labs.thomsonreuters.com/reference/#poe)

## Releases

**Releases should happen through our continuous integration ands deployment process (CI/CD).**
This project is preconfigured to use AWS CodeBuild. See `buildspec.yml`.

**Make sure to update the `CHANGELOG.md` whenever you cut a release.**

---

**This package was generated using the [Python Package Template](https://python.labs.thomsonreuters.com/)**
