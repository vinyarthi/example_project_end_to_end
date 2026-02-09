from __future__ import annotations

import pytest

from app.cli import main


def test_cli_add(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["calc", "add", "2", "3"])
    main()
    out = capsys.readouterr().out.strip()
    assert out == "Result: 5.0"


def test_cli_div_zero_exits(capsys, monkeypatch):
    # argparse's parser.error triggers SystemExit(2)
    monkeypatch.setattr("sys.argv", ["calc", "div", "10", "0"])
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 2
