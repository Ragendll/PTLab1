from src.DataReader import DataReader
from src.Types import DataType


class TextDataReader(DataReader):

    def read(self, path: str) -> DataType:
        students: DataType = {}
        name = ""
        with open(path, encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue
                if not line.startswith(" "):
                    name = line.strip()
                    students[name] = []
                else:
                    if not name:
                        raise ValueError("Предмет указан раньше студента")
                    subject, score = line.split(":", maxsplit=1)
                    students[name].append((subject.strip(), int(score)))
        return students
