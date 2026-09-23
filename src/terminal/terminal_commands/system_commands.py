from terminal.commands.commands_functions import hello_world, about_kalkro, random_100

from terminal.commands.commands_functions.id_commands import show_id, enter_id


system_commands = [
    {"command": "!hello world!", "function": hello_world.hello_world},
    {"command": "!about kalkro!", "function": about_kalkro.about_kalkro},
    {"command": "!random 100!", "function": random_100.random_100},
    {"command": "!show id!", "function": show_id.show_id},
    {"command": "!enter id!", "function": enter_id.enter_id}
]

def help_me():
    for number, system_command in enumerate(system_commands, 1):
        print(f"{number} {system_command['command']}")
        
