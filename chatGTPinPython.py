import openai
openai.api_key = "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"

result = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "user",
            "content": "What is the distance between the earth and mars?"
        }
    ]
)

print(result)