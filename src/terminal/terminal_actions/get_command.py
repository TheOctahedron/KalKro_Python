from utilities.terminal_utilities.terminal_tags import a, b
from utilities.terminal_utilities.terminal_errors import terminal_errors
from terminal.terminal_actions.find_command import find_command

def get_command(obj, cmd): # object, command
    if obj is None:
        print(f"{a}OBJECT: None")
    else:
        print(f"{a}OBJECT: Added")


    if cmd is None:
        print(f"{a}COMMAND: None")
        return f"{b}{terminal_errors[2]}" # ERROR: Command is None.
    else:
        print(f"{a}COMMAND: {cmd}")

    
    if obj is None and cmd is not None:
        return find_command(cmd, None)
    
    elif obj is not None and cmd is not None:
        return find_command(cmd, obj)
    