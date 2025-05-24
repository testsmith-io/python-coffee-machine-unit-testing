from abc import ABC

class Reservoir(ABC):

    def __init__(self, capacity):
        self.capacity = capacity
        self.level = capacity

    def use(self, amount):
        if amount > self.level:
            raise ValueError("Not enough resources!")
        self.level -= amount

    def refill(self, amount):
        self.level = min(self.level + amount, self.capacity)

    def get_level(self):
        return self.level