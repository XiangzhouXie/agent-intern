import asyncio
import httpx


async def fetch(client, url):
    print("开始请求:", url)

    response = await client.get(url)

    print("请求完成:", url)

    return response.status_code

async def main():
    async with httpx.AsyncClient() as client:
        result = await asyncio.gather(
            fetch(client,"https://httpbin.org/get"),
            fetch(client,"https://example.com"),
            fetch(client,"https://www.baidu.com")
        )
        print(result)
asyncio.run(main())