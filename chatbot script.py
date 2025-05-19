#Intent-Based Chatbot using spaCy

import spacy
import random

nlp = spacy.load("en_core_web_sm")

intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning"],
        "responses": ["Hello! How can I assist you?", "Hi there!", "Greetings!"]
    },
    "goodbye": {
        "patterns": ["bye", "see you", "goodbye"],
        "responses": ["Goodbye!", "Take care!", "See you soon!"]
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "thx"],
        "responses": ["You're welcome!", "No problem!", "Glad to help!"]
    }
}

def classify_intent(text):
    doc = nlp(text.lower())
    for intent, data in intents.items():
        for pattern in data['patterns']:
            if pattern in text.lower():
                return intent
    return None

def chatbot_response(text):
    intent = classify_intent(text)
    if intent:
        return random.choice(intents[intent]['responses'])
    return "I'm not sure how to respond to that."

# Chat loop
def chat():
    print("ChatBot:Hi Chaitanya Ask me something! (type 'bye' to quit)")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower():
            print("ChatBot: Goodbye man!")
            break
        print("ChatBot:", chatbot_response(user_input))

if __name__ == "__main__":
    chat()
