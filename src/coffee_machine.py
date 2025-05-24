from enums.coffee_type import CoffeeType
from exceptions.insufficient_beans import InsufficientBeansException
from exceptions.insufficient_milk import InsufficientMilkException
from exceptions.insufficient_water import InsufficientWaterException

class CoffeeMachine:
    def __init__(self, water_tank, bean_reservoir, milk_reservoir):
        self.water_tank = water_tank
        self.bean_reservoir = bean_reservoir
        self.milk_reservoir = milk_reservoir
        self.power_on = False
        self.brew_counts = {coffee_type: 0 for coffee_type in CoffeeType}

    def power_on_machine(self):
        self.power_on = True

    def power_off_machine(self):
        self.power_on = False

    def is_powered_on(self):
        return self.power_on

    def get_brew_count(self, coffee_type):
        return self.brew_counts.get(coffee_type, 0)

    def brew(self, coffee_type):
        if not self.power_on:
            raise RuntimeError("Coffee Machine is OFF. Please turn it ON before brewing.")

        if self.water_tank.get_level() < coffee_type.water_required:
            raise InsufficientWaterException("Not enough water!")
        if self.bean_reservoir.get_level() < coffee_type.beans_required:
            raise InsufficientBeansException("Not enough beans!")
        if self.milk_reservoir.get_level() < coffee_type.milk_required:
            raise InsufficientMilkException("Not enough milk!")

        self.water_tank.use(coffee_type.water_required)
        self.bean_reservoir.use(coffee_type.beans_required)
        self.milk_reservoir.use(coffee_type.milk_required)

        self.brew_counts[coffee_type] += 1
        return f"Your {coffee_type.name.lower()} is ready!"