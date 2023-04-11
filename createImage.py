import openai
openai.api_key = "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"

resultado = openai.Image.create(
    prompt = "A cartoon of a big and strong rooster killing a small and stupid fox",
    n = 1,
    size = "1024x1024"
)

print(resultado)