import argparse

from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader


def get_path_from_arguments(args: list[str]) -> str:
    parser = argparse.ArgumentParser(description="Расчёт рейтинга студентов")
    parser.add_argument("-p", dest="path", required=True,
                        help="Путь к файлу с оценками")
    return parser.parse_args(args).path


def main(args: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Расчёт рейтинга студентов")
    parser.add_argument("-p", dest="path", required=True)
    path = parser.parse_args(args).path
    students = TextDataReader().read(path)
    rating = CalcRating(students).calc()
    print("Рейтинг студентов:")
    for name, score in rating.items():
        print(f"{name}: {score:.2f}")


if __name__ == "__main__":
    main()
