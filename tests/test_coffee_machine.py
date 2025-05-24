import pytest
from enums.coffee_type import CoffeeType
from models.water_tank import WaterTank
from models.bean_reservoir import BeanReservoir
from models.milk_reservoir import MilkReservoir
from coffee_machine import CoffeeMachine
from exceptions.insufficient_water import InsufficientWaterException
from exceptions.insufficient_beans import InsufficientBeansException
from exceptions.insufficient_milk import InsufficientMilkException

def test_initial_power_state_is_false():
    cm = CoffeeMachine(WaterTank(100), BeanReservoir(100), MilkReservoir(100))
    assert cm.is_powered_on() is False 

def test_power_toggle():
    cm = CoffeeMachine(WaterTank(500), BeanReservoir(500), MilkReservoir(500))
    assert cm.is_powered_on() is False 
    cm.power_on_machine()
    assert cm.is_powered_on()
    cm.power_off_machine()
    assert cm.is_powered_on() is False 

def test_brew_without_power():
    cm = CoffeeMachine(WaterTank(500), BeanReservoir(500), MilkReservoir(500))
    with pytest.raises(RuntimeError):
        cm.brew(CoffeeType.COFFEE)

def test_successful_brew():
    cm = CoffeeMachine(WaterTank(500), BeanReservoir(500), MilkReservoir(500))
    cm.power_on_machine()
    msg = cm.brew(CoffeeType.COFFEE)
    assert "Your coffee is ready!" in msg

def test_insufficient_water():
    cm = CoffeeMachine(WaterTank(50), BeanReservoir(500), MilkReservoir(500))
    cm.power_on_machine()
    with pytest.raises(InsufficientWaterException):
        cm.brew(CoffeeType.COFFEE)

def test_insufficient_beans():
    cm = CoffeeMachine(WaterTank(500), BeanReservoir(10), MilkReservoir(500))
    cm.power_on_machine()
    with pytest.raises(InsufficientBeansException):
        cm.brew(CoffeeType.COFFEE)

def test_insufficient_milk():
    cm = CoffeeMachine(WaterTank(500), BeanReservoir(500), MilkReservoir(10))
    cm.power_on_machine()
    with pytest.raises(InsufficientMilkException):
        cm.brew(CoffeeType.CAPPUCCINO)

def test_brew_count():
    cm = CoffeeMachine(WaterTank(1000), BeanReservoir(1000), MilkReservoir(1000))
    cm.power_on_machine()
    cm.brew(CoffeeType.LATTE)
    cm.brew(CoffeeType.LATTE)
    cm.brew(CoffeeType.ESPRESSO)
    assert cm.get_brew_count(CoffeeType.LATTE) == 2
    assert cm.get_brew_count(CoffeeType.ESPRESSO) == 1