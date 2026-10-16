import pytest

from src.TextDataReader import TextDataReader


def test_read(tmp_path):
    path = tmp_path / "students.txt"
    path.write_text("Иванов Иван\n    математика:91\n    физика:100\n"
                    "\nПетров Петр\n    химия:78\n", encoding="utf-8")
    assert TextDataReader().read(str(path)) == {
        "Иванов Иван": [("математика", 91), ("физика", 100)],
        "Петров Петр": [("химия", 78)],
    }


def test_read_empty_file(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_text("", encoding="utf-8")
    assert TextDataReader().read(str(path)) == {}


def test_read_twice(tmp_path):
    first = tmp_path / "first.txt"
    second = tmp_path / "second.txt"
    first.write_text("Иванов\n    математика:80\n", encoding="utf-8")
    second.write_text("Петров\n    физика:90\n", encoding="utf-8")
    reader = TextDataReader()
    reader.read(str(first))
    assert reader.read(str(second)) == {"Петров": [("физика", 90)]}


def test_subject_before_student(tmp_path):
    path = tmp_path / "bad.txt"
    path.write_text("    математика:80\n", encoding="utf-8")
    with pytest.raises(ValueError, match="раньше студента"):
        TextDataReader().read(str(path))


def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        TextDataReader().read(str(tmp_path / "missing.txt"))


def test_invalid_score(tmp_path):
    path = tmp_path / "bad.txt"
    path.write_text("Иванов\n    математика:нет\n", encoding="utf-8")
    with pytest.raises(ValueError):
        TextDataReader().read(str(path))
