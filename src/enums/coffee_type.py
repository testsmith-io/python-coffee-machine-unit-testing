from enum import Enum

class CoffeeType(Enum):
    COFFEE = (200, 20, 0)
    ESPRESSO = (100, 30, 0)
    DOUBLE_ESPRESSO = (150, 40, 0)
    LATTE = (150, 20, 100)
    CAPPUCCINO = (100, 25, 150)
    MACCHIATO = (100, 15, 50)

    @property
    def water_required(self):
        return self.value[0]

    @property
    def beans_required(self):
        return self.value[1]

    @property
    def milk_required(self):
        return self.value[2]
