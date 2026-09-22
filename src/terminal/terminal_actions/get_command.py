from utilities.terminal_utilities.terminal_tags import b
"""
a = [TERMINAL]:
b = [YOU]:
"""

from utilities.terminal_utilities.terminal_errors import terminal_errors
from terminal.terminal_actions.find_command import find_command

def get_command(obj, cmd): # object, command
    if obj is None:
        print(f"{b}OBJECT: None")
    else:
        print(f"{b}OBJECT: Added")


    if cmd is None:
        print(f"{b}COMMAND: None")
        return f"{terminal_errors[0]['command_errors'][2]}" # ERROR: Command is None.
    else:
        print(f"{b}COMMAND: {cmd}")

    if obj is None: 
        return find_command(cmd, None)
    
    elif obj is not None:
        return find_command(cmd, obj)
    
