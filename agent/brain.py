from abc import abstractmethod
from random import choice

from agent.point_of_interest import PointOfInterest


class Brain:

    def __init__(self):
        pass

    @abstractmethod
    def decide_building(self, state):
        pass


class RandomBrain(Brain):
    def __init__(self):
        super().__init__()

    def decide_building(self, state) -> PointOfInterest:
        available_buildings = []
        for building in state.city.points_of_interest:
            if building.is_full():
                continue
            available_buildings.append(building)

        return choice(available_buildings)

