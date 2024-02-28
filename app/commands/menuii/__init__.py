from app.commandhandler import CommandHandler


class MenuCommand:
    def __init__(self):
        self.command_handler = CommandHandler()


    def display_menu(self):
        print("\nAvailable commands:")
        for command in self.command_handler.command_list:
            print(f" - {command}")
        print(" - exit (to quit the application)")
        print("Enter command in the format: command operand1 operand2")