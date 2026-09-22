from file_explorer.explorer_actions.object_actions.select_object import select_object
from utilities.terminal_utilities.terminal_errors import terminal_errors
from terminal.terminal_actions.get_command import get_command
from file_explorer.explorer_actions.object_actions.object_content import object_content

from utilities.terminal_utilities.terminal_tags import a, b
"""
a = [TERMINAL]:
b = [YOU]:
"""

def run_objects_selection(system_folders):
    objects_for_selecting = system_folders
    while True:

        if objects_for_selecting is not system_folders:
            object_content(selected_object) # Show all content in the selected object.


        selected_object = select_object(objects_for_selecting) # Provide the option to select a Object.
        print(f"{b}{selected_object}")
        if selected_object == 0:
            print(f"{a}Exiting object selection.")
            return 0

        object_id = get_command(selected_object, "!show id!") # Get object ID
        if object_id == 0:
            print(f"{a}")

        print(f"\n{b}{object_id}") # Print object ID
        return # funcrion is not complete