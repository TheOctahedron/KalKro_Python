from terminal.commands.commands_storage import system_commands, help_me

def find_command(cmd, obj):
    for system_command in system_commands:
        if cmd == system_command['command']:
            if obj is not None:
                return system_command['function'](obj)
            return system_command['function']()
        
        elif cmd == "!help me!":
            return help_me() 
    return "Command Is Not Found. Write '!HELP ME!'."
