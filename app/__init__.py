from app.commands.add import AddCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand
from app.commands.subtract import SubtractCommand


class App:
    def __init__(self):
        self.command_handler = {}

    def start(self):
        print("Input should be in the format: [command] [operand1] [operand2]")
        print("command -> add/subtract/divide/multiply")
        
        while True:
            user_input = input("Enter command: ")
            if user_input.lower() == 'exit':
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Format: [command] [operand1] [operand2]")
                continue

            command, operand1, operand2 = parts[0].lower(), float(parts[1]), float(parts[2])

            if command == 'add':
                result = AddCommand(operand1, operand2).execute()
            elif command == 'subtract':
                result = SubtractCommand(operand1, operand2).execute()
            elif command == 'multiply':
                result = MultiplyCommand(operand1, operand2).execute()
            elif command == 'divide':
                result = DivideCommand(operand1, operand2).execute()
            else:
                print("Unsupported operation. Please use add, subtract, multiply, or divide.")
                continue

            print(f"Result: {result}")