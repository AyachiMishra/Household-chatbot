# this handles the tasks of adding removing and greeting
from list__manager.list_manager import add_items_to_list, remove_items_from_list, export_list

def handle_add_item(nlp_engine_output):
    items = nlp_engine_output.get('items')
    if not items:
        return ("No item given to add!")
    
    else:
        return add_items_to_list(items)


        

def handle_remove_item(nlp_engine_output):
    items = nlp_engine_output.get('items')
    if not items :
        return "no items given to remove!"
    else:
        return remove_items_from_list(items)

def handle_export_list():
    return export_list()




def handle_greet_user():
    return ("HEllo! i can help you manage your grocery list. Try adding or removing any items! ")