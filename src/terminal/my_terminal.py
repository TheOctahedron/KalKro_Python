from terminal.commands.commands_storage import find_command

a = "[TERMINAL]: "
b = "\n[YOU]: "

def my_terminal():
    print(f"{a}Welcome to KalKro.")
    while True:
        cmd = input(f"\n{a}Press F to open File Explorer.{b}").strip().lower()
        match cmd:
            case "f":
                pass
            case _:
                find_command(cmd)
                continue