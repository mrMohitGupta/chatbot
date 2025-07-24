# Import the required libraries
import openai
import gradio

# Set your OpenAI API key
openai.api_key = "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"

# Define the initial system message
messages = [{"role": "system", "content": "A  Helpful AI Assistant"}]


# Define the chatbot function
def CustomChatGPT(user_input):
    # Append the user's input to the messages list
    messages.append({"role": "user", "content": user_input})

    # Use the OpenAI API to get the chatbot's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract the chatbot's reply from the API response
    ChatGPT_reply = response["choices"][0]["message"]["content"]

    # Append the chatbot's reply to the messages list
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    # Return the chatbot's response
    return ChatGPT_reply


# Create the Gradio interface
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="CHATBOT by GOKUL Mohit")

# Launch the Gradio interface
demo.launch(share=True)
