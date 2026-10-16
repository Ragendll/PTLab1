import argparse
from pathlib import Path
import sys

from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader
from src.XmlDataReader import XmlDataReader


def get_path_from_arguments(args: list[str]) -> str:
    parser = argparse.ArgumentParser(description="Расчёт рейтинга студентов")
    parser.add_argument("-p", dest="path", required=True,
                        help="Путь к TXT или XML с оценками")
    return parser.parse_args(args).path


def main(args: list[str] | None = None) -> None:
    if args is None:
        args = sys.argv[1:]
    path = get_path_from_arguments(args)
    extension = Path(path).suffix.lower()
    if extension == ".txt":
        reader = TextDataReader()
    elif extension == ".xml":
        reader = XmlDataReader()
    else:
        raise ValueError("Поддерживаются только TXT и XML")
    students = reader.read(path)
    rating = CalcRating(students).calc()
    print("Рейтинг студентов:")
    for name, score in rating.items():
        print(f"{name}: {score:.2f}")


if __name__ == "__main__":
    main()
