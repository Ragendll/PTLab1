from pathlib import Path
from xml.etree.ElementTree import ParseError

import pytest

from src.TextDataReader import TextDataReader
from src.XmlDataReader import XmlDataReader


@pytest.fixture
def xml_path(tmp_path):
    path = tmp_path / "students.xml"
    path.write_text(
        '<students><student name="Иванов Иван">'
        '<subject name="высшая математика">91</subject>'
        '<subject name="физика">100</subject>'
        '</student><student name="Петров">'
        '<subject name="химия">78</subject></student></students>',
        encoding="utf-8",
    )
    return str(path)


def test_read(xml_path):
    assert XmlDataReader().read(xml_path) == {
        "Иванов Иван": [("высшая математика", 91), ("физика", 100)],
        "Петров": [("химия", 78)],
    }


def test_read_twice(xml_path, tmp_path):
    reader = XmlDataReader()
    reader.read(xml_path)
    path = tmp_path / "empty.xml"
    path.write_text("<students/>", encoding="utf-8")
    assert reader.read(str(path)) == {}


@pytest.mark.parametrize("text, error", [
    ("<students>", ParseError),
    ("<root/>", ValueError),
    ('<students><student/></students>', KeyError),
    ('<students><student name=" "/></students>', ValueError),
    ('<students><student name="Иванов"/>'
     '<student name="Иванов"/></students>', ValueError),
    ('<students><student name="Иванов">'
     '<subject name="физика">нет</subject></student></students>', ValueError),
    ('<students><student name="Иванов">'
     '<subject name="физика"/></student></students>', ValueError),
])
def test_invalid_xml(tmp_path, text, error):
    path = tmp_path / "bad.xml"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(error):
        XmlDataReader().read(str(path))


def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        XmlDataReader().read(str(tmp_path / "missing.xml"))


def test_examples_have_same_data():
    data_dir = Path(__file__).resolve().parents[1] / "data"
    assert XmlDataReader().read(str(data_dir / "data.xml")) == (
        TextDataReader().read(str(data_dir / "data.txt"))
    )
