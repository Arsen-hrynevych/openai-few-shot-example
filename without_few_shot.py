from os import environ

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    organization=environ["OPENAI_ORGANIZATION"],
    project=environ["OPENAI_PROJECT"],
    api_key=environ["OPENAI_API_KEY"],
)

completion_response = client.chat.completions.create(
    model=environ['OPENAI_MODEL'],
    messages=[
        {
            "role": "user",
            "content": "Summarize the following text: The quick brown fox jumps over the lazy dog.",
        }
    ],
)

print(completion_response.choices[0].message.content)
