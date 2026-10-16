import pytest

from src.FirstQuartile import FirstQuartile


@pytest.mark.parametrize("rating, expected", [
    ({}, {}),
    ({"А": 80}, {"А": 80}),
    ({"А": 80, "Б": 60}, {"Б": 60}),
    ({"А": 10, "Б": 20, "В": 30}, {"А": 10}),
    ({"А": 40, "Б": 10, "В": 30, "Г": 20}, {"Б": 10}),
    ({"А": 10, "Б": 20, "В": 30, "Г": 40, "Д": 50},
     {"А": 10, "Б": 20}),
    ({"А": 60, "Б": 60, "В": 80, "Г": 100}, {"А": 60, "Б": 60}),
    ({"А": 80, "Б": 80, "В": 80, "Г": 80},
     {"А": 80, "Б": 80, "В": 80, "Г": 80}),
    ({"А": 60.25, "Б": 60.75, "В": 70.5, "Г": 90.0}, {"А": 60.25}),
])
def test_calc(rating, expected):
    assert FirstQuartile(rating).calc() == expected


def test_example_distribution():
    rating = dict(zip("АБВГДЕЖЗ", [55, 65, 70, 75, 82, 83.6667, 90, 95]))
    # Q1 = 65 + 0.75 * (70 - 65) = 68.75.
    assert FirstQuartile(rating).calc() == {"А": 55, "Б": 65}
