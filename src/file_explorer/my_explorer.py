from file_explorer.explorer_actions.folder_actions.show_folders import show_folders
from file_explorer.explorer_actions.folder_actions.select_folder import select_folder
from terminal.terminal_actions.get_command import get_command
from file_explorer.explorer_actions.file_actions.show_files import show_files
from utilities.user_input import user_input

def my_explorer():
    print("EXPLORER\n\n")
    show_folders() # Showing all folders
    while True:
        print("\n\nACTIONS IN FILE EXPLORER:")
        print("(0) Exit. (to Terminal)")
        print("(1) Select Folder and File.")
        answer = user_input("\n\nEnter the number of the selected action") 
        match answer:
            case "0":
                return # Leave to Terminal.

            case "1":
                selected_folder = select_folder() # Provide the option to select a folder.
                folder_id = get_command(selected_folder, "!show id!")
                print(folder_id)

                show_files(selected_folder) # Show all files in the selected folder.
                # TODO: write function select_file
                continue

            case _:
                print("Action Number Is not Found.")
                continue
