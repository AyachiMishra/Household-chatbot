from .handlers import handle_add_item, handle_remove_item, handle_greet_user, handle_export_list

def dispatch(nlp_engine_output):

    intent = nlp_engine_output.get("intent")
    items = nlp_engine_output.get("items")

    if intent == "ADD_ITEM":
        return handle_add_item(nlp_engine_output)
    
    
    elif intent == 'REMOVE_ITEM':
        return handle_remove_item(nlp_engine_output)
    
    elif intent == 'GREET':
        return handle_greet_user()
    
    elif intent == 'EXPORT_LIST':
        return handle_export_list()
    
    
    else:
        return "sorry, i couldn't understand that! Could you please rephrase your sentence or state it preferabely in english?"




