from utilities.terminal_utilities.terminal_tags import a, b
from terminal.terminal_actions.get_command import get_command
from file_explorer.my_explorer import my_explorer

def welcome_to_terminal():
    print(f"{a}Welcome to KalKro.")
    while True:
        cmd = input(f"\n{a}Press F to open File Explorer.\n{b}").strip().lower()
        match cmd:
            case "f":
                my_explorer()
            case _:
                answer = get_command(None, cmd)
                print(answer)
                continue
