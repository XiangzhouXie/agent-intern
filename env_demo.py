import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MY_API_KEY")

print(api_key)