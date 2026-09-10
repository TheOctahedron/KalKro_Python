from terminal.commands.commands_functions import hello_world, about_kalkro, random_100

system_commands = [
    {"command": "!hello world!", "function": hello_world},
    {"command": "!about kalkro!", "function": about_kalkro},
    {"command": "!random 100!", "function": random_100}
]

def help_me():
    for number, system_command in enumerate(system_commands, 1):
        print(f"{number} {system_command['command']}")
        

def find_command(cmd):
    for system_command in system_commands:
        if cmd == system_command['command']:
            return system_command['function']()
        elif cmd == "!help me!":
            return help_me() 
    return "Command Is Not Found. Write '!HELP ME!'."