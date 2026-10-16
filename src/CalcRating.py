from src.Types import DataType, RatingType


class CalcRating:

    def __init__(self, data: DataType) -> None:
        self.data = data

    def calc(self) -> RatingType:
        rating: RatingType = {}
        for name, subjects in self.data.items():
            if not subjects:
                raise ValueError(f"У студента {name} нет оценок")
            total = 0
            for subject, score in subjects:
                total += score
            rating[name] = total / len(subjects)
        return rating
