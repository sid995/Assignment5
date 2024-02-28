from app.commands.add import AddCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand
from app.commands.subtract import SubtractCommand
from app.commands import CommandHandler

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.command_handler.register_command("add", AddCommand)
        self.command_handler.register_command("subtract", SubtractCommand)
        self.command_handler.register_command("divide", DivideCommand)
        self.command_handler.register_command("multiply", MultiplyCommand)

    def start(self):
        print("Input should be in the format: [command] [operand1] [operand2]")
        print("Please use add, subtract, multiply, or divide.")
        
        while True:
            user_input = input("Enter command: ")
            if user_input.lower() == 'exit':
                break

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Format: [command] [operand1] [operand2]")
            else:
                command, operand1, operand2 = parts[0].lower(), float(parts[1]), float(parts[2])
                match command:
                    case 'add':
                        result = AddCommand(operand1, operand2).execute()    
                    case 'subtract':
                        result = SubtractCommand(operand1, operand2).execute()
                    case 'multiply':
                        result = MultiplyCommand(operand1, operand2).execute()
                    case 'divide':
                        result = DivideCommand(operand1, operand2).execute()
                    case _:
                        print("Unsupported operation. Please use add, subtract, multiply, or divide.")

                print(f"Result: {result}")