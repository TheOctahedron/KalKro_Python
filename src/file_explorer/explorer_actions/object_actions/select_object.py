from utilities.user_input import user_input
from utilities.terminal_utilities.terminal_errors import terminal_errors

def select_object(objects_list): 
    """
    Get a list of all the objects we can select.
    """
    while True:
        selected_object = user_input("Write the number of the Selected Object.")
        if selected_object == 0:
            return 0
        
        try:
            selected_object = int(selected_object)
        except ValueError:
            print("Error. Please re-read the input requirements.")
            continue


        for number, obj in enumerate(objects_list, 1):

            if selected_object == number:
                selected_object = obj
                return selected_object
        
        print(terminal_errors[0]['object_errors'][1]) # ERROR: Object is not Found.
        continue
