import json

def load_current_list():
    with open('data/current_list.json', 'r') as f:
        current_list = json.load(f)

    return current_list

def save_current_list(updated_list):
    with open('data/current_list.json', 'w') as f:
        json.dump(updated_list, f, indent=2)


def add_items_to_list(items):
    current_list = load_current_list()
    for item in items:
        if not item in current_list:
            current_list.append(item)
            print("succesfully added", item, "to the list! happy listing!")


        
        else:
            print(item ,"is already added in the list")

    save_current_list(current_list)
    
    return "Anything else to be added to the list?"




def remove_items_from_list(items):
    current_list = load_current_list()
    for item in items:
        if not item in current_list:
            print("This is item is already not there in the list!")
            


        else:
            current_list.remove(item)
            print("succesfully removed", item, "from the list! happy listing!")

    save_current_list(current_list)

    return "Anything else to be removed from the list?"



def export_list():
    current_list = load_current_list()
    with open('exports/exported_list.txt', 'w') as f:
        for item in current_list:
            f.write(item + '\n')
    return "Exported list successfully!"


def give_current_list():
    current_list = load_current_list()
    print(current_list)



