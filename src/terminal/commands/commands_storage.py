from terminal.commands.commands_functions import hello_world, about_kalkro, random_100, show_selected_folder, enter_id


system_commands = [
    {"command": "!hello world!", "function": hello_world.hello_world},
    {"command": "!about kalkro!", "function": about_kalkro.about_kalkro},
    {"command": "!random 100!", "function": random_100.random_100},
    {"command": "!show selected folder!", "function": show_selected_folder.show_selected_folder},
    {"command": "!enter id!", "function": enter_id.enter_id}
]

def help_me():
    for number, system_command in enumerate(system_commands, 1):
        print(f"{number} {system_command['command']}")
        