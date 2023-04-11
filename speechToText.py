import openai
openai.api_key = "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"

audio_file = open("audio/german1.mp3", "rb")
result = openai.Audio.translate("whisper-1", audio_file)

print(result)