from abc import abstractmethod


class FulfilledNeed:

    def __init__(self):
        pass

    @abstractmethod
    def get_score(self) -> int:
        pass


class Water(FulfilledNeed):
    def get_score(self) -> int:
        return 30


class Food(FulfilledNeed):
    def get_score(self) -> int:
        return 20


class Shelter(FulfilledNeed):
    def get_score(self) -> int:
        return 10
