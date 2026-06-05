from badges import cli


def test_cli_add(capsys) -> None:
    exit_code = cli.main(["add", "1.5", "2.5"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "4.0"
    assert captured.err == ""


def test_cli_subtract(capsys) -> None:
    exit_code = cli.main(["subtract", "10", "3"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "7.0"
    assert captured.err == ""


def test_cli_divide(capsys) -> None:
    exit_code = cli.main(["divide", "9", "3"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "3.0"
    assert captured.err == ""


def test_cli_divide_by_zero(capsys) -> None:
    exit_code = cli.main(["divide", "1", "0"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == ""
    assert "division by zero" in captured.err.lower()
