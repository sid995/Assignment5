from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_add_command_execute():
    command = AddCommand(1, 2)
    assert command.execute() == 3

def test_subtract_command_execute():
    command = SubtractCommand(5, 3)
    assert command.execute() == 2

def test_multiply_command_execute():
    command = MultiplyCommand(3, 4)
    assert command.execute() == 12

def test_divide_command_execute():
    command = DivideCommand(8, 2)
    assert command.execute() == 4

def test_divide_by_zero():
    command = DivideCommand(5, 0)
    assert command.execute() == "Error: Division by zero"