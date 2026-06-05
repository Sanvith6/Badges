import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "badges.cli", *args],
        check=False,
        capture_output=True,
        text=True,
    )


def test_cli_add() -> None:
    result = run_cli("add", "1.5", "2.5")
    assert result.returncode == 0
    assert result.stdout.strip() == "4.0"


def test_cli_subtract() -> None:
    result = run_cli("subtract", "10", "3")
    assert result.returncode == 0
    assert result.stdout.strip() == "7.0"


def test_cli_divide() -> None:
    result = run_cli("divide", "9", "3")
    assert result.returncode == 0
    assert result.stdout.strip() == "3.0"


def test_cli_divide_by_zero() -> None:
    result = run_cli("divide", "1", "0")
    assert result.returncode == 1
    assert "division by zero" in result.stderr.lower()
