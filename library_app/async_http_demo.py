import asyncio
import time
import httpx

def sync_fetch(name:str,seconds:int)->None:
    print(name,"同步开始")
    response = httpx.get(f"https://httpbin.org/delay/{seconds}")
    print(name,"同步完成")
    print("状态码：",response.status_code)

async def fetch(
    client: httpx.AsyncClient,
    name: str,
    seconds: int
) -> None:

    print(name, "异步开始")

    response = await client.get(
        f"https://httpbin.org/delay/{seconds}"
    )

    print(name, "完成，状态码:", response.status_code)

def run_sync():
    start = time.time()
    sync_fetch("请求A",3)
    sync_fetch("请求B",2)
    sync_fetch("请求C",1)
    end = time.time()
    print("同步总耗时:", end - start)
async def run_async():
    start = time.time()

    async with httpx.AsyncClient(timeout=10) as client:

        await asyncio.gather(
            fetch(client, "请求A", 3),
            fetch(client, "请求B", 2),
            fetch(client, "请求C", 1)
        )

    end = time.time()

    print("异步总耗时:", end - start)

run_sync()
asyncio.run(run_async())