import httpx
import json
def get_user(user_id:int):
    try:
        response = httpx.get(url = f"https://jsonplaceholder.typicode.com/users/{user_id}")
        print(response.status_code)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        print("捕获异常:",e)
        return None
def save_user(user:dict,user_id:int):
    with open(f"user_{user_id}.json","w") as file:
        json.dump(user,file)

user = get_user(1)
if user is not None:
    save_user(user,1) 