import httpx
try:
    response = httpx.get("https://httpbin.org/status/404")
    print("状态码:",response.status_code)
    response.raise_for_status()
    print("请求成功")
except httpx.RequestError as e:
    print("网络请求失败:",e)
except httpx.HTTPStatusError as e:
    print("服务器返回错误状态码:",e.response.status_code)
