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
    model=environ["OPENAI_MODEL"],
    messages=[
        {
            "role": "system",
            "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.",
        },
        {
            "role": "user",
            "content": "Summarize the following text:\n"
            "Text: A cat climbed a tree and was rescued by firefighters.\n"
            "Summary: Cat rescued from a tree.\n\n"
            "Text: A team of researchers discovered a new species of frog in the Amazon rainforest.\n"
            "Summary: New frog species found in Amazon.\n\n"
            "Text: The quick brown fox jumps over the lazy dog.\n"
            "Summary:",
        },
    ],
)

print(completion_response.choices[0].message.content)
