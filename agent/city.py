from typing import List

from agent.agent import RandomResident
from agent.point_of_interest import Farm, Fountain, Home, PointOfInterest


class City:
    def __init__(self):
        self.residents = [RandomResident(), RandomResident()]
        self.points_of_interest: List[PointOfInterest] = [Fountain(), Farm(), Home(2)]