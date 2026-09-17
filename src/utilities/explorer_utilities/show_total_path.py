total_path = []


def show_total_path(part, type, position):
    """
    'folder'/'subfolder' have a '/' guide sign
    Other types of objects are marked with a dot and the name of the type.
    """
    match type:
        case "folder", "subfolder":
           part += "/" 
        case _:
            part += type


    """
    '>' - FORWARD
    '<' - BACK
    """
    match position:
        case ">": 
            total_path.append(part)
        case "<": 
            total_path.remove(part)
    
    print(f"PATH: {total_path}")