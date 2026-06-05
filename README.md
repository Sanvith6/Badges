# Badges
Minimal Python utilities with CI, security automation, and release badges baked in.

![CI](https://github.com/Sanvith6/Badges/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/Sanvith6/Badges/actions/workflows/codeql.yml/badge.svg)
![codecov](https://codecov.io/gh/Sanvith6/Badges/branch/main/graph/badge.svg)
![License](https://img.shields.io/github/license/Sanvith6/Badges)
![Release](https://img.shields.io/github/v/release/Sanvith6/Badges)
![PyPI](https://img.shields.io/pypi/v/badges)
![Contributors](https://img.shields.io/github/contributors/Sanvith6/Badges)
![Issues](https://img.shields.io/github/issues/Sanvith6/Badges)
![Pull Requests](https://img.shields.io/github/issues-pr/Sanvith6/Badges)
![GitHub last commit](https://img.shields.io/github/last-commit/Sanvith6/Badges)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/Sanvith6/Badges/ci.yml?event=push)
![GitHub Discussions](https://img.shields.io/github/discussions/Sanvith6/Badges)

## Installation
```bash
pip install badges
```

## Usage
### Library
```python
from badges import add, divide, subtract

add(1, 2)
subtract(10, 3)
divide(9, 3)
```

### CLI
```bash
badges add 1 2
badges subtract 10 3
badges divide 9 3
```

## Development
```bash
pip install -e .[dev]
ruff check .
pytest
```

## Coverage Policy
CI fails if total test coverage drops below 90%.

## Documentation
- Architecture: [docs/architecture.md](docs/architecture.md)
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## Security
See [SECURITY.md](SECURITY.md) for reporting guidelines.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and PR guidance.

## Roadmap
- Add more arithmetic operations.
- Expand CLI output formatting options.
- Publish typed stubs and API docs.

## Repository Activation Steps
1. Set repository visibility to **Public**.
2. Enable **Issues**, **Discussions**, **Wiki** (optional), and **GitHub Actions**.
3. Add repository topics: `python`, `pytest`, `github-actions`, `badges`, `codeql`, `codecov`, `pypi`, `oss`.
4. In **Settings > Code security**, enable CodeQL default setup if needed.
5. Add repository secret `CODECOV_TOKEN`.
6. Protect `main` with required status checks (CI + CodeQL).
7. Create the first semantic version tag: `v0.1.0`.
8. Create a GitHub Release from the `v0.1.0` tag.
9. Publish the package to PyPI (trusted publishing).
10. Verify all badge URLs return 200 and display in README.
