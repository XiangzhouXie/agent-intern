import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.responses.create(
    model="deepseek-v4-flash",
    input=[
        {"role": "system", "content": "你是一个资深 Python 面试官，只回答核心原理，不举例"},
        {"role":"user","content":"什么是 asyncio.gather?"}
        ]
)

print(response.output_text)