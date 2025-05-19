# AI-CHATBOT-WITH-NLP
# API-INTEGRATION-AND-DATA-VISUALIZATION
* COMPANY : CODTECH IT SOLUTIONS
* NAME : SURU CHAITANYA
* INTERN ID : CT08DA121
* DOMAIN : PYTHON PROGRAMMING
* DURATION : 8 WEEKS
* MENTOR : NEELA SANTOSH

## DESCRIPTION OF THIS PROJECT

This Python program demonstrates a simple AI chatbot that uses Natural Language Processing (NLP) via the spaCy library to understand and respond to user queries. The chatbot classifies the user's input into predefined "intents" based on keywords and then selects an appropriate response.

The system operates using basic rule-based pattern matching within user inputs to determine the intent. Once an intent is matched, the chatbot chooses a random response from a list of associated replies, creating the effect of a human-like conversation.

## Key Features:
Utilizes spaCy for robust and efficient text processing.

Matches user inputs to predefined intents (e.g., greeting, thanks, goodbye).

Supports multiple phrases for each intent to improve accuracy.

Chooses random responses from a list to simulate variation.

Easy to extend with more intents and responses.

## Technologies Used:
Python – Programming language

spaCy – NLP library for tokenization and language modeling

Random – To vary responses for each matched intent

## How It Works:
The chatbot loads the English NLP model from spaCy (en_core_web_sm).

It defines a set of intents, each with:

patterns: keywords or phrases that trigger the intent.

responses: possible replies.

When a user enters a message:

The message is converted to lowercase and processed using spaCy.

The input is matched to an intent by checking if any pattern is present.

If a match is found, the chatbot returns a random response from that intent.

If no intent matches, it returns a default fallback message.

## OUTPUT

## Example Use Case:

User: Hi
ChatBot: Hi there!

User: Thank you
ChatBot: No problem!

User: Bye
ChatBot: Goodbye!

