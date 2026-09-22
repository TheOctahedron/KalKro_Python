from utilities.folders import folders

def system_folders():
    while True: 
        if folders == None:
            print("You don't have any folders.")
            input("Press Enter To Exit.")
            return
        print("\n\nSYSTEM FOLDERS:")
        for number, folder in enumerate(folders, 1):
            print(f"[{number}] {folder['name']}")
        print("\nEND OF FOLDERS.")
        break
    return folders 
