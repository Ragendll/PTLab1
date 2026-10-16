from xml.etree import ElementTree

from src.DataReader import DataReader
from src.Types import DataType


class XmlDataReader(DataReader):

    def read(self, path: str) -> DataType:
        root = ElementTree.parse(path).getroot()
        if root.tag != "students":
            raise ValueError("Корневой элемент должен называться students")

        students: DataType = {}
        for student in root.findall("student"):
            name = student.attrib["name"].strip()
            if not name:
                raise ValueError("Не указано имя студента")
            if name in students:
                raise ValueError(f"Студент {name} указан повторно")
            students[name] = []
            for subject in student.findall("subject"):
                title = subject.attrib["name"].strip()
                score = int(subject.text or "")
                students[name].append((title, score))
        return students
