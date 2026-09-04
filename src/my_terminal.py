from commands import find_command

a = "[TERMINAL]: "
b = "\n[YOU]: "

def my_terminal():
    print(f"{a}Welcome to KalKro.")
    while True:
        cmd = input(f"{a}Press F to open File Explorer.{b}").strip().upper()
        match cmd:
            case "F":
                pass
            case _:
                answer = find_command(cmd)
                print(answer)
                continue