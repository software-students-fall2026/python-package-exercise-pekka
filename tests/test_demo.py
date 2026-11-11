import runpy
from pathlib import Path

DEMO_PATH = Path(__file__).resolve().parent.parent / "examples" / "demo.py"


def run_demo(capsys):
    runpy.run_path(str(DEMO_PATH), run_name="__main__")
    return capsys.readouterr().out


def test_demo_runs_without_errors(capsys):
    output = run_demo(capsys)

    assert len(output.strip()) > 0


def test_demo_shows_every_function(capsys):
    output = run_demo(capsys)

    assert "generate_fact" in output
    assert "generate_history" in output
    assert "generate_statistic" in output
    assert "generate_discovery" in output


def test_demo_shows_an_invalid_input_error(capsys):
    output = run_demo(capsys)

    assert "ValueError" in output
