from file_explorer.explorer_actions.object_actions.select_object import select_object
from utilities.terminal_utilities.terminal_errors import terminal_errors
from terminal.terminal_actions.get_command import get_command
from file_explorer.explorer_actions.object_actions.show_object_content import show_object_content

from utilities.terminal_utilities.terminal_tags import a, b
"""
a = [TERMINAL]:
b = [YOU]:
"""

def run_objects_selection(system_folders):
    selectable_object = {
        "name": "SYSTEM FOLDERS",
        "content": system_folders,
        "type": ".folder"
    }
    
    while True:
        # We check if the object is empty; if so, we notify accordingly and exit."""
        if selectable_object['content'] is None:
            print("You don't have any folders.")
            input("Press Enter To Exit.")
            return 0



        # We get the object's ID and display it.
        object_id = get_command(selectable_object, "!show id!") # Get object ID
        if object_id == 0:
            print(f"{a}{terminal_errors[0]['id_errors'][1]}")
            return 0
        print(f"\n{b}{object_id}") # Print object ID




        # We show the contents of the object (so the user can select something if it is a folder).
        show_object_content(selectable_object)




        # If the object is a folder, we ask the user to select a file from it for further processing.
        if selectable_object['type'] == ".folder":

            selected_object = select_object(selectable_object['content']) # Provide the option to select a Object.
            print(f"{b}{selected_object}")
            if selected_object == 0:
                print(f"{a}Exiting object selection.")
                return 0
            selectable_object = selected_object
            continue


        return
