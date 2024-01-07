#Getting started

#Cleaning WhatsApp conversation data in a separate file (cleaner.py)

#Importing the cleaning function and training the chatbot 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Chatpot")

from cleaner import clean_corpus
CORPUS_FILE = "/Users/fatimaisaeva/Downloads/materials-chatterbot-2/source_code_step_3/chat.txt"
chatbot = ChatBot("Chatpot")
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer = ListTrainer(chatbot)
trainer.train(cleaned_corpus)

#How to exit the bot
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")