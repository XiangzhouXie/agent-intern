import httpx
import os
from dotenv import load_dotenv
load_dotenv()
def search_book(keyword:str)->dict:
    params = {"keyword":keyword}
    response = httpx.get("https://httpbin.org/get",params=params)
    return response.json()

def borrow_book(name:str)->dict:
    token = os.getenv("MY_API_KEY")
    data = {"name":name}
    headers ={"authorization":token}
    response = httpx.post("https://httpbin.org/post",json=data,headers=headers)
    return response.json()