# Architecture

## Module Layout
- `badges.core` contains the pure arithmetic functions.
- `badges.cli` exposes the command-line interface and wires arguments to the
  core functions.

## Extension Points
- Add new operations in `badges.core` and register them in `badges.cli`.
- Extend the CLI by adding new subcommands and tests in `tests/test_cli.py`.
