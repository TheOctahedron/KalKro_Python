def show_object_content(selected_object):
    print(f"SELECTED OBJECT: {selected_object['name']}")

    if selected_object['type'] is ".folder":
        print(f"\n{selected_object['name']} CONTENT: ")
        for number, obj in enumerate(selected_object['content']):
            print(f"[{number}] {obj['name']}{obj['type']}")
            print(f"\nEND OF {selected_object['name']}.")
        
    for file_content in selected_object['content']:
        print(f"\nFILE CONTENT: ")
        print(file_content)
        print("\nEND OF FILE-CONTENT.")
    
    return
