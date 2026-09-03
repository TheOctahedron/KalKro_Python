a = "[TERMINAL]: "
b = "\n[YOU]: "

def my_terminal():
    print(f"{a}Welcome to KalKro.")
    cmd = input(f"{a}Press F to open File Explorer.{b}").upper()
    match cmd:
        case "F":
            pass
        case _:
            pass