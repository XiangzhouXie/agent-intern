import time
import asyncio
async def task(name:str,seconds:int)->None:
    print(name,"开始")
    await asyncio.sleep(seconds)
    print(name,"完成")
async def main():
    start = time.time()
    await asyncio.gather(
        task("任务A",3),
        task("任务B",2),
        task("任务C",1)
    )
    end = time.time()
    print("总耗时:",end-start)

asyncio.run(main())