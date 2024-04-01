import nltk
import random
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ["I'm good, thank you!", "I'm doing well, thanks!"]),
    (r'what is your name?', ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"]),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'(.*)', ["I'm sorry, I didn't understand that.", "Could you please repeat that?"])
]

# Create a ChatBot instance
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Welcome to the chatbot! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    else:
        print("ChatBot:", chatbot.respond(user_input))
