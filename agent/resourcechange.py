from abc import abstractmethod


class Resource:

    @abstractmethod
    def is_used_in_step(self):
        pass

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Resource):
            return self.__class__.__name__ == other.__class__.__name__
        return False

    def __hash__(self):
        return hash(self.__class__.__name__)


class Water(Resource):

    def is_used_in_step(self):
        return True


class Food(Resource):

    def is_used_in_step(self):
        return True


class ResourceChange:

    def __init__(self, resource: Resource, amount: int):
        self.resource = resource
        self.amount = amount
