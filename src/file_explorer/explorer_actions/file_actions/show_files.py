from utilities.folders import folders

def show_files(selected_folder):
    print(f"SELECTED FOLDER: {selected_folder['name']}")
    for file in selected_folder['entries']:
        print(f"{file['name']}{file['type']}")
    return # The function is incomplete.
