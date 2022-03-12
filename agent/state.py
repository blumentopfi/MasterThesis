from agent.city import City


class State:
    def __init__(self):
        self.city = City()

    def step(self):
        print("STEP")
        for resident in self.city.residents:
            if resident.location is not None:
                continue
            resident.step(self)

        for building in self.city.points_of_interest:
            building.step()

        for resident in self.city.residents:
            print(f"{resident.name} has achieved a score of: {resident.calculate_performance()}")