import pytest

from src.main import get_path_from_arguments, main


def test_correct_arguments():
    assert get_path_from_arguments(["-p", "data/data.txt"]) == "data/data.txt"


def test_path_with_spaces():
    assert get_path_from_arguments(["-p", "my data/file.txt"]) == (
        "my data/file.txt"
    )


@pytest.mark.parametrize("args", [[], ["data/data.txt"], ["-p"]])
def test_incorrect_arguments(args):
    with pytest.raises(SystemExit) as error:
        get_path_from_arguments(args)
    assert error.value.code == 2


def test_main(tmp_path, capsys):
    path = tmp_path / "students.txt"
    path.write_text("Иванов\n    математика:80\n", encoding="utf-8")
    main(["-p", str(path)])
    assert "Иванов: 80.00" in capsys.readouterr().out


def test_main_xml(tmp_path, capsys):
    path = tmp_path / "students.XML"
    path.write_text('<students><student name="Иванов">'
                    '<subject name="физика">90</subject>'
                    '</student></students>', encoding="utf-8")
    main(["-p", str(path)])
    assert "Иванов: 90.00" in capsys.readouterr().out


def test_unknown_format():
    with pytest.raises(ValueError, match="TXT и XML"):
        main(["-p", "data.json"])
