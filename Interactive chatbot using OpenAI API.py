import openai

# Set your OpenAI API key
openai.api_key = "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"

# Initialize an empty list to store chat messages
messages = []

# Prompt the user to specify the type of chatbot they want to create
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

# Inform the user that the chatbot is ready
print("Your new assistant is ready!")

# Start a loop to keep the conversation going until the user types "quit()"
while True:
    message = input()  # Take input from the user
    messages.append({"role": "user", "content": message})  # Add user message to the list of messages
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5-turbo model for chat completion
        messages=messages)  # Send the list of messages to OpenAI API
    reply = response["choices"][0]["message"]["content"]  # Get the assistant's reply from the API response
    messages.append({"role": "assistant", "content": reply})  # Add assistant's reply to the list of messages
    print("\n" + reply + "\n")