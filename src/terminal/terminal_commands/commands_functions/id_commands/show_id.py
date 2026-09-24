from utilities.terminal_utilities.terminal_errors import terminal_errors


def show_id(obj):
    try:
        if obj is None:
            return terminal_errors[0]['object_errors'][2]
        return f"ID: {obj['id']}"
    except (TypeError, KeyError):
        return terminal_errors[0]['object_errors'][2]
