Chosen stack: Python with pytest.

Placeholder values to replace before use:
- {OWNER}: GitHub account or organization name.
- {REPO}: GitHub repository name.
- {PROJECT_NAME}: Python package/module name.
- {PYPI_PACKAGE}: Published package name on PyPI.

1. Stage 1 — Initialize repository foundation
Goal/badges enabled: License badge, Python version badge, repo quality/community readiness.
Exact Copilot instruction to generate files/changes (paste-ready prompt text):
```text
Create the initial Python library repository scaffold for a public open-source project named "{PROJECT_NAME}".

Requirements:
- Use src layout.
- Create pyproject.toml with setuptools build backend, project metadata, and pytest/ruff config.
- Add README.md with placeholder sections (do not add final badge block yet).
- Keep LICENSE as MIT.
- Add .gitignore for Python artifacts.
- Add CODE_OF_CONDUCT.md, CONTRIBUTING.md, SECURITY.md.
- Add .editorconfig.
- Commit with message: "chore: initialize python project foundation".
```
Files to create with brief expected contents:
- pyproject.toml — package metadata, build system, pytest and coverage settings.
- .editorconfig — consistent formatting rules.
- CODE_OF_CONDUCT.md — Contributor Covenant summary.
- CONTRIBUTING.md — setup, test, and PR steps.
- SECURITY.md — vulnerability reporting policy.
Example badge markdown lines that should be added to README (exact text):
```md
![License](https://img.shields.io/github/license/{OWNER}/{REPO})
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Repo Size](https://img.shields.io/github/repo-size/{OWNER}/{REPO})
```

2. Stage 2 — Add minimal library and CLI with tests
Goal/badges enabled: Test status badge, pytest badge, basic package usefulness.
Exact Copilot instruction to generate files/changes (paste-ready prompt text):
```text
Implement a minimal but complete Python package called {PROJECT_NAME} with:
- src/{PROJECT_NAME}/core.py containing pure functions:
  - add(a: float, b: float) -> float
  - subtract(a: float, b: float) -> float
  - divide(a: float, b: float) -> float (raise ValueError on division by zero)
- src/{PROJECT_NAME}/cli.py with argparse commands: add, subtract, divide.
- src/{PROJECT_NAME}/__init__.py exporting functions.
- tests/test_core.py covering success and error paths.
- tests/test_cli.py validating CLI output and exit codes.
Target >= 90% coverage from tests.
Commit with message: "feat: add core module, cli, and pytest suite".
```
Files to create with brief expected contents:
- src/{PROJECT_NAME}/core.py — core arithmetic logic with safe divide.
- src/{PROJECT_NAME}/cli.py — command-line interface.
- src/{PROJECT_NAME}/__init__.py — public exports.
- tests/test_core.py — unit tests for all functions and edge cases.
- tests/test_cli.py — CLI tests using subprocess or pytest capsys.
Example badge markdown lines that should be added to README (exact text):
```md
![Tests](https://img.shields.io/badge/tests-pytest-informational)
```

3. Stage 3 — Add GitHub Actions CI + coverage upload
Goal/badges enabled: Build/CI badge, coverage badge, GitHub Actions badge.
Exact Copilot instruction to generate files/changes (paste-ready prompt text):
````text
Create GitHub Actions CI workflow at .github/workflows/ci.yml.
Use this exact YAML:

```yaml
name: CI
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e .[dev]
      - name: Lint
        run: ruff check .
      - name: Test with coverage threshold
        run: pytest --cov={PROJECT_NAME} --cov-report=xml --cov-report=term-missing --cov-fail-under=90
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage.xml
          fail_ci_if_error: true
          token: ${{ secrets.CODECOV_TOKEN }}
```

Also add pytest-cov to dev dependencies in pyproject.toml.
Commit with message: "ci: add github actions workflow with coverage enforcement".
Note: CODECOV_TOKEN must be configured (see Stage 8, step 5) before coverage uploads will succeed.
Optional: move the coverage threshold into pyproject.toml to keep one source of truth.
````
Files to create with brief expected contents:
- .github/workflows/ci.yml — matrix CI, lint, tests, coverage upload.
- pyproject.toml — updated dev dependencies for ruff/pytest/pytest-cov.
Example badge markdown lines that should be added to README (exact text):
```md
![CI](https://github.com/{OWNER}/{REPO}/actions/workflows/ci.yml/badge.svg)
![codecov](https://codecov.io/gh/{OWNER}/{REPO}/branch/main/graph/badge.svg)
```

4. Stage 4 — Add security automation (CodeQL + Dependabot)
Goal/badges enabled: CodeQL badge, Dependabot badge, security policy credibility.
Exact Copilot instruction to generate files/changes (paste-ready prompt text):
````text
Add security automation files.

1) Create .github/workflows/codeql.yml with this YAML:
```yaml
name: "CodeQL"
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
  schedule:
    - cron: "23 3 * * 1" # Weekly Monday scan at 03:23 UTC; adjust as needed
jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    strategy:
      fail-fast: false
      matrix:
        language: ["python"]
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: ${{ matrix.language }}
      - name: Autobuild
        uses: github/codeql-action/autobuild@v3
      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
```

2) Create .github/dependabot.yml with this YAML:
```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

Commit with message: "security: add codeql and dependabot automation".
````
Files to create with brief expected contents:
- .github/workflows/codeql.yml — static analysis workflow.
- .github/dependabot.yml — dependency update policy.
Example badge markdown lines that should be added to README (exact text):
```md
![CodeQL](https://github.com/{OWNER}/{REPO}/actions/workflows/codeql.yml/badge.svg)
![Dependabot](https://img.shields.io/badge/dependabot-enabled-025E8C?logo=dependabot)
```

5. Stage 5 — Add release automation and package publishing
Goal/badges enabled: Release badge, PyPI version badge, publish workflow badge.
Exact Copilot instruction to generate files/changes (paste-ready prompt text):
````text
Set up automated release publishing.

1) Create .github/workflows/release.yml:
```yaml
name: Release
on:
  push:
    tags:
      - "v*.*.*"
jobs:
  build-and-publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install build tools
        run: |
          python -m pip install --upgrade pip
          pip install build
      - name: Build package
        run: python -m build
      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
```

2) Ensure pyproject.toml contains version (e.g., 0.1.0) and project URLs.
3) Add CHANGELOG.md with Keep a Changelog format and Semantic Versioning notes.
4) Configure PyPI Trusted Publisher before first release (PyPI project settings -> Publishing -> Add a new publisher for this repo/workflow).
Commit with message: "release: add tag-triggered pypi publishing workflow".
````
Files to create with brief expected contents:
- .github/workflows/release.yml — publish package when tag is pushed.
- CHANGELOG.md — changelog and semver policy.
- pyproject.toml — version and URL metadata.
Example badge markdown lines that should be added to README (exact text):
```md
![Release](https://img.shields.io/github/v/release/{OWNER}/{REPO})
![PyPI](https://img.shields.io/pypi/v/{PYPI_PACKAGE})
```

6. Stage 6 — Add community health and issue/PR templates
Goal/badges enabled: Community profile completeness, contributor friendliness badges.
Exact Copilot instruction to generate files/changes (paste-ready prompt text):
```text
Create community files and templates:
- .github/ISSUE_TEMPLATE/bug_report.yml
- .github/ISSUE_TEMPLATE/feature_request.yml
- .github/pull_request_template.md
- .github/SUPPORT.md

Use GitHub issue forms YAML format with required fields.
Include reproduction steps for bugs and proposal/use-case fields for features.
In pull_request_template.md include checklist for tests, docs, and changelog updates.
Commit with message: "docs: add issue and pull request templates".
```
Files to create with brief expected contents:
- .github/ISSUE_TEMPLATE/bug_report.yml — structured bug report form.
- .github/ISSUE_TEMPLATE/feature_request.yml — structured feature request form.
- .github/pull_request_template.md — PR checklist.
- .github/SUPPORT.md — support channels.
Example badge markdown lines that should be added to README (exact text):
```md
![Contributors](https://img.shields.io/github/contributors/{OWNER}/{REPO})
![Issues](https://img.shields.io/github/issues/{OWNER}/{REPO})
![Pull Requests](https://img.shields.io/github/issues-pr/{OWNER}/{REPO})
```

7. Stage 7 — Final README badge block, usage docs, and quality checks
Goal/badges enabled: README quality badges, docs completeness, project discoverability.
Exact Copilot instruction to generate files/changes (paste-ready prompt text):
```text
Rewrite README.md into a polished open-source landing page including:
- Project title and one-line value proposition
- Badge block at top (CI, CodeQL, Codecov, License, Release, PyPI, Contributors)
- Installation section (pip install {PYPI_PACKAGE})
- Usage examples for library and CLI
- Development section (lint/test commands)
- Coverage policy statement (CI fails if coverage < 90%)
- Security and contribution links
- Roadmap section

Also add docs/architecture.md describing module layout.
Commit with message: "docs: finalize readme badges and developer documentation".
```
Files to create with brief expected contents:
- README.md — complete documentation with badge block.
- docs/architecture.md — package architecture and extension points.
Example badge markdown lines that should be added to README (exact text):
```md
![CI](https://github.com/{OWNER}/{REPO}/actions/workflows/ci.yml/badge.svg)
![CodeQL](https://github.com/{OWNER}/{REPO}/actions/workflows/codeql.yml/badge.svg)
![codecov](https://codecov.io/gh/{OWNER}/{REPO}/branch/main/graph/badge.svg)
![License](https://img.shields.io/github/license/{OWNER}/{REPO})
![Release](https://img.shields.io/github/v/release/{OWNER}/{REPO})
![PyPI](https://img.shields.io/pypi/v/{PYPI_PACKAGE})
![Contributors](https://img.shields.io/github/contributors/{OWNER}/{REPO})
```

8. Stage 8 — Repository settings, topics, and badge activation checklist
Goal/badges enabled: Public repo/program badges, active workflow badges, release badges.
Exact Copilot instruction to generate files/changes (paste-ready prompt text):
```text
Provide a final operator checklist in README.md called "Repository Activation Steps" with exact manual actions:
1) Set repository visibility to Public.
2) Enable Issues, Discussions, Wiki (optional), and GitHub Actions.
3) Add repository topics: python, pytest, github-actions, badges, codeql, codecov, pypi, oss.
4) In Settings > Code security, enable CodeQL default setup if needed.
5) Add repository secret CODECOV_TOKEN.
6) Protect main branch with required status checks (CI + CodeQL).
7) Create first semantic version tag: v0.1.0.
8) Create a GitHub Release from v0.1.0 tag.
9) Publish package to PyPI (trusted publishing).
10) Verify all badge URLs return 200 and display in README.

Then commit with message: "docs: add repository activation checklist for badges".
```
Files to create with brief expected contents:
- README.md — final activation checklist appended.
Example badge markdown lines that should be added to README (exact text):
```md
![GitHub last commit](https://img.shields.io/github/last-commit/{OWNER}/{REPO})
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/{OWNER}/{REPO}/ci.yml?event=push)
![GitHub Discussions](https://img.shields.io/github/discussions/{OWNER}/{REPO})
```
