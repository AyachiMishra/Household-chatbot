# bot should be able to add, remove, remind that this is already included in the list
# bot should be able to get meaning of the word and not be taught on hardcoded words
# bot should eb able ot get quantity of the item too

# input would come(as text)
# we clean the input, remove stop words and then need to fit the menaing of rest of words
# we return the processed list
# now from the processed list we haev to find the intent
# into whether they mean add, remove, check, and also on which list
# recognise the item nd also its quantity
# recognise in case there is no quantity and leave it blank



import spacy
from spacy.lang.en.stop_words import STOP_WORDS 

nlp = spacy.load("en_core_web_sm")

'''Preprocess Function: This function'''
def preprocess(text):
    doc = nlp(text.lower())

    processed_list = [token.lemma_ for token in doc if  not token.is_punct]
    return ' '.join(processed_list)


class NLP_ENGINE():
    def __init__(self):

        # initialise a dictionary where each key(an intent) and gets mapped to a list of its synonyms
        # if a word in the given sentence matches that intent's syninyms, the intetnt is aved using intent_classfiication method
        self.intent_map = {'ADD_ITEM': ["add", "buy", "purchase", "get", "khareed",'khareedna','kharidna','laana','lana' ,"le aana"], 
              
                           'REMOVE_ITEM': ["remove", "delete", "cancel", "cut", "drop",
                                           "hatado", "hatao", "hata dena", "nikal do", "nikalo", "delete karo"],
                            "CHECK_BUDGET": ["budget", "kitna", "kharch", "remaining", "how much", "left", "paise"], 
                            "SWITCH_LIST": ["switch", "change", "dusri list", "campus list", "home list", "jao", "set active"],
                            "GREET": ["hi", "hello", "hey", "good morning", "good evening","namaste", "pranam", "salaam", "yo", "hey bot"],
                            "EXPORT_LIST": ["send", "export", "share", "download", "save","bhej do", 'bhejo',"bhejna", "send karo",
                                             "list bhejo", "pdf", 'bhej de' 'send me']}

    #identify the intent
    def intent_classification(self, text):
        processed_text = preprocess(text)

        # .items() method of dictionaries return a view object that displays a LIST of the dictionaries' KEY VALUE tuple pairs
        for intent, keywords in self.intent_map.items():
            for phrase in keywords:
                if phrase in processed_text:
                    return intent
        else:
            return 'UNKNOWN'
        

    def entity_detection(self, given_text):
        processed_text_1 = preprocess(given_text)
        doc = nlp(processed_text_1)
        hinglish_verbs = {"le", "aana", "ja", "le aana", "la", "laana", "do", "bhej", "nikal",'bhai', 'list','bhaiya'}

        items = []
        
        for token in doc:
            if (token.pos_ == "NOUN" or token.pos_ == 'PROPN') and token.text.lower() not in hinglish_verbs:
                items.append(token.text)

        return items
    
    '''parse function: We will now use all the previously defined functions to identify and extract useful information(which is the
    intent and the entity from) from given text input. These include identifying the intent, the entity using the defined functions ,
    map them in a dictionary and return it, ready to  be used for the next module.'''
    def parse(self, text2):
        item = self.entity_detection(text2)
        intent = self.intent_classification(text2)
        if intent in ['ADD_ITEM', 'REMOVE_ITEM']:
            return {'intent': intent, 'items': item}
        else:
            return {'intent': intent}

    



# INTENT_DETECTION:

        # Best would be to use the in operator on the whole string, then wwe will not need to use looping
        # using .items to get an iterable with both keys and values of the dictionary
        # if you dont find the intent, return unknown