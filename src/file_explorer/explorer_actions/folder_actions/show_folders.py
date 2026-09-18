from utilities.folders import folders

def show_folders():
    while True: 
        if folders == None:
            print("You don't have any folders.")
            input("Press Enter To Exit.")
            return
        print("\n\nFOLDERS:")
        for number, folder in enumerate(folders, 1):
            print(f"[{number}] {folder['name']}")
        print("\nend of folders.")
        break
    return
