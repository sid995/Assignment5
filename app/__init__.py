from app.commands.add import AddCommand
from app.commands.divide import DivideCommand
from app.commands.multiply import MultiplyCommand
from app.commands.subtract import SubtractCommand
from app.commands.menu import MenuCommand
from app.commandhandler import CommandHandler


class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.register_commands()


    def register_commands(self):
        self.command_handler.register_command('add', AddCommand)
        self.command_handler.register_command('subtract', SubtractCommand)
        self.command_handler.register_command('multiply', MultiplyCommand)
        self.command_handler.register_command('divide', DivideCommand)
        self.command_handler.register_command('menu', MenuCommand(list(self.command_handler.get_keys())))


    def get_user_input(self):
        return input("\nEnter command: ").strip().lower()


    def parse_input(self, input_str):
        parts = input_str.split()
        if parts[0] == "menu":
            return parts[0], None, None
        if len(parts) != 3:
            raise ValueError("Invalid input format. Expected: command operand1 operand2")
        return parts[0], float(parts[1]), float(parts[2])
    

    def display_menu(self):
        self.command_handler.execute_command("menu", None, None)


    def run(self):
        self.display_menu()
        while True:
            user_input = self.get_user_input()
            if user_input == 'exit':
                print("Exiting App")
                break

            try:
                command, *operands = self.parse_input(user_input)
                if command == 'menu':
                    self.display_menu()
                else:
                    operands = list(map(float, operands))
                    result = self.command_handler.execute_command(command, *operands)
                    print(f"Result: {result}")
            except Exception as e:
                print(e)
