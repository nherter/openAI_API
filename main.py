"""

main.py
17.03.2025

loads .env and extracts OPENAI_API_KEY

"""
# Libraries

import os
from dotenv import load_dotenv, dotenv_values
from openai import OpenAI

# Parameters
QUESTION = "What is the capital of France?"
SYSTEM_PROMPT = """
You are a helpful assistant that translates questions to answers, 
add a emoji to the end of the answer related to the question,
answer in a single sentence,
Answer in Japanese.
"""

# Load the .env file
load_dotenv()

# Extract the API key from the .env file
API_KEY = os.getenv("OPENAI_API_KEY")

# Create the OpenAI Client
client = OpenAI(api_key=API_KEY)

# Define the OpenAI Model
MODEL = "gpt-4o-mini"

#Define the OpenAI Massage
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": QUESTION},
]

# Create the OpenAI Client
res = client.chat.completions.create(
    model=MODEL,
    messages=messages,
)

# Print the response
print(res.choices[0].message.content)
print(res.usage)
