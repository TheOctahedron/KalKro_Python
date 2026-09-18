from utilities.terminal_utilities.terminal_errors import terminal_errors


def show_id(obj_name, storage):
    if obj_name == None:
        return terminal_errors[0]['object_errors'][2]
    for object in storage:
        if object['name'] == obj_name:
            return f"ID: {object['id']}"
    return "Object is not Found."
