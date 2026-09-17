from utilities.explorer_utilities.folders import folders
from utilities.terminal_utilities.terminal_errors import terminal_errors


def show_selected_folder(obj):
    if obj == None:
        return terminal_errors[0]['object_errors'][2]
    for folder in folders:
        if folder['name'] == obj:
            return f"NAME: {folder['name']}\nID: {folder['id']}"
    return "Folder is not Found."
