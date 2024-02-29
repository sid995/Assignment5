from app.commands import Command

class ModCommand(Command):
    command_name = 'mod'

    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b

    def execute(self) -> float:
        return self.operand_a % self.operand_b