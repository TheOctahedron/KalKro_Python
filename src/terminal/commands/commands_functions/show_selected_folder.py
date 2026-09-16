from file_explorer.shorcuts_structure import folders

def show_selected_folder(obj):
    for folder in folders:
        if folder['name'] == obj:
            return f"NAME: {folder['name']}\nID: {folder['id']}"
    return "Folder is not Found."
