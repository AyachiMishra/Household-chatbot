from nlp_engine.nlp_engine import NLP_ENGINE
from dispatcher.dispatcher import dispatch


message = input()

data = NLP_ENGINE()
intent_data = data.parse(message)
response = dispatch(intent_data)

print(response)



