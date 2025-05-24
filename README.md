# ☕ Coffee Machine Simulator - Python Version

A **Python-based coffee machine simulation**, featuring OOP principles, custom exceptions, full unit test coverage, and mutation testing.

## 🚀 Features
- Multiple coffee types: Espresso, Latte, etc.
- Reservoir management (water, beans, milk)
- Custom exceptions for resource issues
- 100% test coverage using `pytest`
- Mutation testing with `mutmut`

## 📁 Project Structure
```plaintext
coffee_machine/
    enums/
    exceptions/
    models/
    coffee_machine.py
    tests/
README.md
```

## ⚙️ Setup & Usage
```bash
pip install -r requirements.txt
pytest --cov=coffee_machine tests/
mutmut run
mutmut results
```

## ☕ Menu
| Coffee Type       | Water | Beans | Milk |
|------------------|--------|--------|-------|
| Espresso         | 100ml | 30g   | 0ml   |
| Double Espresso  | 150ml | 40g   | 0ml   |
| Coffee           | 200ml | 20g   | 0ml   |
| Latte            | 150ml | 20g   | 100ml |
| Cappuccino       | 100ml | 25g   | 150ml |
| Macchiato        | 100ml | 15g   | 50ml  |

To run mutation tests, ensure `mutmut` is installed and configured properly. Enjoy testing your virtual coffee machine!

## Coverage

| Name                                                                     | Stmts | Miss Branch BrPart | Cover |   |      |
|--------------------------------------------------------------------------|-------|--------------------|-------|---|------|
| ------------------------------------------------------------------------ |       |                    |       |   |      |
| src/coffee_machine.py                                                    | 33    | 0                  | 8     | 0 | 100% |
| src/enums/__init__.py                                                    | 0     | 0                  | 0     | 0 | 100% |
| src/enums/coffee_type.py                                                 | 12    | 0                  | 0     | 0 | 100% |
| src/exceptions/__init__.py                                               | 0     | 0                  | 0     | 0 | 100% |
| src/exceptions/insufficient_beans.py                                     | 2     | 0                  | 0     | 0 | 100% |
| src/exceptions/insufficient_milk.py                                      | 2     | 0                  | 0     | 0 | 100% |
| src/exceptions/insufficient_water.py                                     | 2     | 0                  | 0     | 0 | 100% |
| src/models/__init__.py                                                   | 0     | 0                  | 0     | 0 | 100% |
| src/models/bean_reservoir.py                                             | 3     | 0                  | 0     | 0 | 100% |
| src/models/milk_reservoir.py                                             | 3     | 0                  | 0     | 0 | 100% |
| src/models/reservoir.py                                                  | 13    | 2                  | 2     | 1 | 80%  |
| src/models/water_tank.py                                                 | 3     | 0                  | 0     | 0 | 100% |
| tests/__init__.py                                                        | 0     | 0                  | 0     | 0 | 100% |
| tests/test_coffee_machine.py                                             | 48    | 0                  | 0     | 0 | 100% |
| ------------------------------------------------------------------------ |       |                    |       |   |      |
| TOTAL                                                                    | 121   | 2                  | 10    | 1 | 98%  |
