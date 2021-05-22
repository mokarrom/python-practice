<!--
    MAKE AN AWESOME README!
    https://dbader.org/blog/write-a-great-readme-for-your-github-project
    https://github.com/dbader/readme-template
    https://github.com/matiassingers/awesome-readme
    https://www.makeareadme.com/
-->

# misc

> Python Practice Code

<!-- Placeholders https://shields.io -->
<!-- [![Python 3][python3]][python3]
[![Build Status][buildstatus]][buildstatus]
[![Tests][teststatus]][teststatus]
[![Coverage][coverage]][coverage] -->

## Installation

### Install from source

Clone this repository. Then have `poetry` create a virtual environment and install all dependencies into it.

```
poetry install
```

### Install from package index

<!-- TODO update when package publishing is configured -->
*This package is not yet published to a package index.*

[Learn how to publish this package](https://python.labs.thomsonreuters.com/publishing/publish-your-package/)

## Usage

### Virtual environment usage

Assuming you're using TR's standard `poetry`, you can activate and execute commands within the virtual environment anytime using `poetry run` or `poetry shell`.

```
$ poetry run <command>
```

```
$ poetry shell
$ <command>
```

[Learn how to use `poetry`](https://python.labs.thomsonreuters.com/reference/#poetry)

### Library usage

<!-- TODO add poetry run, poetry shell -->

```
from misc import misc
```

### Command line usage

```bash
$ misc
misc version 0.1.0

USAGE
  0.1.0 [-h] [-q] [-v [<...>]] [-V] [--ansi] [--no-ansi] [-n] <command> [<arg1>] ... [<argN>]
...
```

## Documentation

### Documentation from source

[Install from source](#install-from-source). Then run the `host-local-docs` task.

```
poetry run poe host-local-docs
```

### Remotely deployed documentation

<!-- TODO update when documenation is deployed remotely -->
*This package's documentation is not yet deployed remotely.*

[Learn how to deploy this package's documentation](https://python.labs.thomsonreuters.com/documentation/deploy-docs/#deploy-for-others)

## Resources

* [LICENSE](LICENSE.md)
* [CHANGELOG](CHANGELOG.md)
* [CONTRIBUTING](CONTRIBUTING.md)
* [DEVELOPERS](DEVELOPERS.md)


---

**This package was generated using the [Python Package Template](https://python.labs.thomsonreuters.com/)**

<!-- Markdown link & img dfn's -->
<!-- [python3]: https://img.shields.io/badge/python-v3.8-blue
[buildstatus]: https://img.shields.io/badge/build-passing-brightgreen
[teststatus]: https://img.shields.io/badge/tests-✔%2020%20%7C%20✘%201%20%7C%20➟%201-red
[coverage]: https://img.shields.io/badge/coverage-86%25-yellowgreen -->
