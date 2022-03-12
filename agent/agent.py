from agent.brain import Brain, RandomBrain
from agent.resourcechange import ResourceChange, Resource, Water, Food
import names


class Resident:

    def __init__(self, brain: Brain):
        self.resources = {}
        self.sheltered = False
        self.brain = brain
        self.location = None
        self.name = names.get_first_name()

    def __has_sufficient_resources(self, resource: Resource, min_amount: int) -> bool:
        if resource not in self.resources:
            return False
        return self.resources[resource] > min_amount

    def is_thirsty(self) -> bool:
        return not self.__has_sufficient_resources(Water(), 0)

    def is_hungry(self):
        return not self.__has_sufficient_resources(Food(), 0)

    def calculate_performance(self):
        score = 0
        if self.sheltered:
            score += 20
        if not self.is_thirsty():
            score += 50
        if not self.is_hungry():
            score += 30
        return score

    def step(self, state):
        building = self.brain.decide_building(state)
        building.join(self)

        print(f"{self.name} joined {building.__class__.__name__}")

        for resource, amount in self.resources.items():
            if resource.is_used_in_step():
                self.resources[resource] = amount - 1

    def add_resource(self, resource_change: ResourceChange):
        new_amount = resource_change.amount
        if resource_change.resource in self.resources:
            new_amount += resource_change.amount

        self.resources[resource_change.resource] = new_amount


class RandomResident(Resident):

    def __init__(self):
        super().__init__(RandomBrain())
