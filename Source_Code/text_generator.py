import os
from openai import OpenAI

api_key = "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"

if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)
model_engine = "gpt-3.5-turbo-0125"

text = input("What topic you want to write about: ")
prompt = text
print("The AI BOT is trying now to generate a new text for you...")

chat_completion = client.chat.completions.create(
    model=model_engine,
    messages=[
        {
            "role": "user",
            "content": prompt, 
        }
    ],
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
generated_text = chat_completion.choices[0].message.content
print(generated_text.strip())

with open("generated_text.txt", "w") as file:
    file.write(generated_text.strip())
print("The Text Has Been Generated Successfully!")