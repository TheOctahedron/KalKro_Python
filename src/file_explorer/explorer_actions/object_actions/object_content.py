from utilities.folders import folders

def object_content(selected_object):
    print(f"SELECTED OBJECT: {selected_object['name']}")
    if selected_object['type'] is ".folder":
        print("\nFOLDER CONTENT: ")
        for number, obj in enumerate(selected_object['content']):
            print(f"[{number}] {obj['name']}{obj['type']}")
            print("\nEND OF FOLDER-CONTENT.")
        print(f"{obj['name']}{obj['type']}")
        
    for file_content in selected_object['content']:
        print(f"\nFILE CONTENT: ")
        print(file_content)
        print("\nEND OF FILE-CONTENT.")
    
    return 
