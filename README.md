# Few-shot Learning with OpenAI API

## 🚀 Project Overview

This is a simple Python script demonstrating how to use the OpenAI API to generate chat completions using the `gpt` model. This project showcases the few-shot learning technique, where the model is prompted with a limited number of examples to generate relevant responses.

## 📂 Project Structure

```
few-shot-training/
│
├── few_shot_example.py       # Script demonstrating few-shot learning with OpenAI API
├── without_few_shot.py       # Script showing API usage without few-shot learning
├── README.md                  # Project documentation and instructions
├── .env                       # Environment variables for API access
├── .env.template              # Template for environment variables
```

## 📋 Prerequisites

- Python 3.12+
- OpenAI API access
- Environment with necessary credentials

## 🔧 Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Arsen-hrynevych/openai-few-shot-example
   cd openai-few-shot-example
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required dependencies:
   ```bash
   pip install openai python-dotenv
   ```

4. Create a `.env` file in the project root with the following variables:
   ```
   OPENAI_ORGANIZATION=your_organization_id
   OPENAI_PROJECT=your_project_id
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_MODEL=your_model
   ```

## 🌟 Usage

Run the script:
```bash
python few_shot_example.py  # To see few-shot learning in action
# or
python without_few_shot.py  # To see basic usage without few-shot learning
```

### Example Code: few_shot_example.py

Here is the code from `few_shot_example.py` that demonstrates how to interact with the OpenAI API using few-shot learning:

```python
from os import environ
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    organization=environ["OPENAI_ORGANIZATION"],
    project=environ["OPENAI_PROJECT"],
    api_key=environ["OPENAI_API_KEY"]
)

message_request = client.chat.completions.create(
    model=environ['OPENAI_MODEL'],
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
print(message_request)
```

In this example, the model is given two examples of text summarization before being asked to summarize a new text. This demonstrates few-shot learning, where the model learns from the provided examples to generate a similar style of summary for the new input.

## 📖 Few-Shot Learning Technique

In this project, we utilize the few-shot learning technique to demonstrate how the model can generate responses based on a limited number of examples. This approach allows the model to leverage its inherent knowledge while being tailored to specific tasks with minimal input.

### How Few-Shot Learning Works
Few-shot learning involves providing the model with a few examples to guide its responses. In our case, we will use the `few_shot_example.py` file to show how the model generates responses based on example prompts.

## 🔑 Environment Variables

- `OPENAI_ORGANIZATION`: Your OpenAI organization ID
- `OPENAI_PROJECT`: Your OpenAI project ID
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_MODEL`: The model to use

## 📦 Dependencies

- `openai`: OpenAI Python library
- `python-dotenv`: Loads environment variables from a .env file

## ⚠️ Important Notes

- Keep your `.env` file private and never commit it to version control
- Ensure you have a valid OpenAI API key and sufficient credits

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b type/feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'type: Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
