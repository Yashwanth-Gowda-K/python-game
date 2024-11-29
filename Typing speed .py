import random
import nltk
from nltk.chat.util import Chat, reflections

# Pairs of input and response
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"],
    ],
    [
        r"what is your name\??",
        ["I am a simple chatbot. You can call me Bot!", "I'm Bot, your virtual assistant."],
    ],
    [
        r"how are you\??",
        ["I'm just a program, but I'm functioning as expected!", "Doing great, thanks for asking!"],
    ],
    [
        r"what can you do\??",
        [
            "I can chat with you, answer basic questions, and keep you company!",
            "I am here to provide simple assistance and information.",
        ],
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a nice day!", "See you later! Take care!"],
    ],
    [
        r"(.*) your (.*)",
        ["Why do you want to know about my %2?", "Let's not focus on my %2."],
    ],
    [
        r"(.*) help (.*)",
        ["I am here to help you. What do you need assistance with?", "Tell me how I can assist you."],
    ],
    [
        r"(.*) created you\??",
        ["I was created by a programmer learning Python.", "A Python enthusiast created me!"],
    ],
]

# Reflection dictionary for handling pronouns
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

# Function to start chatbot
def chatbot():
    print("Bot: Hi! I am a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download("punkt")  # Required for processing text with NLTK
    chatbot()
