from utilities.user_input import user_input
from file_explorer.explorer_actions.object_actions.show_object_content import show_object_content
from file_explorer.explorer_actions.object_actions.run_objects_selection import run_objects_selection
from utilities.explorer_utilities.folders import folders

def my_explorer():
    while True:
        print("EXPLORER\n\n")
        system_folders = {
            "name": "SYSTEM FOLDERS",
            "content": folders,
            "type": ".folder"
        }
        show_object_content(system_folders) # Showing all system folders
        print("\n\nACTIONS IN FILE EXPLORER:")
        print("(0) Exit. (to Terminal)")
        print("(1) Select Folder and File.")
        answer = str(user_input("\n\nEnter the number of the selected action"))
        match answer:
            case "0":
                return # Leave to Terminal.

            case "1":
                run_objects_selection(system_folders)

            case _:
                print("Action Number Is not Found.")
                continue
