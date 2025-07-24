import openai

openai.api_key = "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"  # Insert your own openai API secret key

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me ideas for apps and services I could build with openai apis"}])
print(completion.choices[0].message.content)

# Change the content prompt as per your way