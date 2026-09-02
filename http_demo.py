import httpx

headers = {
    "X-Student": "Xiangzhou"
}

response = httpx.get(
    "https://httpbin.org/get",
    headers=headers
)

data = response.json()

print(data["headers"])