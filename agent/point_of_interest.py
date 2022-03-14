from abc import abstractmethod

from agent.needs import Shelter
from agent.resourcechange import Resource, ResourceChange, Water, Food


class PointOfInterest:

    def __init__(self, capacity):
        self.capacity = capacity
        self.residents_at_location = {}

    @abstractmethod
    def step(self):
        pass

    def is_full(self):
        return len(self.residents_at_location) >= self.capacity

    def join(self, resident):
        resident.location = self
        self.residents_at_location[resident] = 0


class Home(PointOfInterest):

    def step(self):
        residents_to_delete = []

        for owner in self.owners:
            owner.fulfill_need(Shelter())

        for resident in self.residents_at_location:
            residents_to_delete.append(resident)
            resident.location = None
            resident.fulfill_need(Shelter())

        for resident in residents_to_delete:
            del self.residents_at_location[resident]

    def join(self, resident):
        super(Home, self).join(resident)
        if len(self.owners) < self.capacity:
            self.owners.append(resident)

    def __init__(self, capacity):
        super().__init__(capacity)

        self.owners = []


class ResourceProducer(PointOfInterest):

    def __init__(self, duration: int, capacity: int, resource: Resource, amount: int):
        self.resource = resource
        self.amount = amount
        self.duration_in_building = duration
        super().__init__(capacity)

    def step(self):
        change = ResourceChange(self.resource, self.amount)
        residents_to_delete = []

        for resident, duration in self.residents_at_location.items():

            if duration + 1 > self.duration_in_building:
                resident.add_resource(change)
                print(f"Produced {self.amount} of {self.resource.__class__.__name__} for {resident.name} in {self.__class__.__name__}")

                residents_to_delete.append(resident)
                resident.location = None
            else:
                self.residents_at_location[resident] = duration + 1

        for resident in residents_to_delete:
            del self.residents_at_location[resident]


class Fountain(ResourceProducer):
    def __init__(self):
        super().__init__(1, 1, Water(), 1)


class Farm(ResourceProducer):
    def __init__(self):
        super().__init__(5, 1, Food(), 5)
