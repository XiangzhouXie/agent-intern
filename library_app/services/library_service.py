import httpx
import os
from dotenv import load_dotenv
load_dotenv()
def search_book(keyword:str)->dict:
    params = {"keyword":keyword}
    try:
        response = httpx.get("https://httpbin.org/get",params=params)
        print("查书状态码：",response.status_code)
        return response.json()
    except httpx.RequestError as e:
        print("网络请求失败:",e)
        return None
    except httpx.HTTPStatusError as e:
        print("服务器返回错误状态码:",e.response.status_code)
        return None

def borrow_book(name:str)->dict:
    token = os.getenv("MY_API_KEY")
    data = {"name":name}
    headers ={"authorization":token}
    try:
        response = httpx.post("https://httpbin.org/post",json=data,headers=headers)
        print("借书状态码：",response.status_code)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        print("网络请求失败:",e)
        return None
    except httpx.HTTPStatusError as e:
        print("服务器返回错误状态码:",e.response.status_code)
        return None
