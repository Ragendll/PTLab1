from statistics import quantiles

from src.Types import RatingType


class FirstQuartile:

    def __init__(self, rating: RatingType) -> None:
        self.rating = rating

    def calc(self) -> RatingType:
        if not self.rating:
            return {}
        scores = list(self.rating.values())
        if len(scores) == 1:
            boundary = scores[0]
        else:
            boundary = quantiles(scores, n=4, method="inclusive")[0]

        students: RatingType = {}
        for name, score in self.rating.items():
            if score <= boundary:
                students[name] = score
        return students
