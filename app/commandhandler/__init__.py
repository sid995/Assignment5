from app.commands import Command


class CommandHandler:
    def __init__(self):
        self.command = Command()
        self.command_list = {}
    

    def register_command(self, command_name: str, command_class: Command):
        self.command_list[command_name] = command_class


    def execute_command(self, command_name, *operands):
        if command_name not in self.command_list:
            raise ValueError(f"Unsupported command: {command_name}")

        command = self.command_list[command_name]
        
        if isinstance(command, type):
            command_instance = command(*operands)
            return command_instance.execute()
        else:
            return command.execute()

    
    
    def get_keys(self):
        return self.command_list.keys()