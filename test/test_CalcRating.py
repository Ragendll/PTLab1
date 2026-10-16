import pytest

from src.CalcRating import CalcRating


def test_calc():
    data = {
        "Иванов": [("математика", 80), ("физика", 76), ("химия", 100)],
        "Петров": [("математика", 61), ("физика", 80)],
    }
    rating = CalcRating(data).calc()
    assert rating == pytest.approx({"Иванов": 85.333333, "Петров": 70.5})


def test_empty_data():
    assert CalcRating({}).calc() == {}


def test_student_without_scores():
    with pytest.raises(ValueError, match="нет оценок"):
        CalcRating({"Иванов": []}).calc()


def test_calc_does_not_keep_previous_result():
    data = {"Иванов": [("математика", 80)]}
    calculator = CalcRating(data)
    assert calculator.calc() == {"Иванов": 80.0}
    data.clear()
    assert calculator.calc() == {}
