from utilities.user_input import user_input
from utilities.folders import folders

def select_folder():
    """
    We ask for the number of the selected folder from the list.
    """
    while True:
        selected_folder = user_input("Write the number of the Selected Folder.")
        if selected_folder == 0:
            return 0
        
        try:
            selected_folder = int(selected_folder)
        except Exception as e:
            print(e)
            continue


        found = False

        for number, folder in enumerate(folders, 1):

            if selected_folder == number:
                selected_folder = folder
                found = True

        if found == False:
            print("Folder is Not Found.")
            continue

        break
    
    return selected_folder
