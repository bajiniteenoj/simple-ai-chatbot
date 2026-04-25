# Simple AI Chatbot
# Author: Teenoj

print("🤖 Simple AI Chatbot")
print("Type 'exit' to stop the chatbot")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break

    elif "hello" in user_input:
        print("Chatbot: Hello! How can I help you?")

    elif "your name" in user_input:
        print("Chatbot: I am Teenoj's AI chatbot.")

    elif "how are you" in user_input:
        print("Chatbot: I'm doing great!")

    elif "bye" in user_input:
        print("Chatbot: See you later!")

    else:
        print("Chatbot: Sorry, I don't understand that.")