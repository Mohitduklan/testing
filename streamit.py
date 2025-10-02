import asyncio

async def a():
    await asyncio.sleep(3)
    return "a"

async def b():
    await asyncio.sleep(5)
    return "b"

async def c():
    await asyncio.sleep(10)
    return "c"

async def main():
    result = ""
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(a())
        t2 = tg.create_task(b())
        t3 = tg.create_task(c())
        tasks = pending = [t1, t2, t3]
        
        # while not any([t1.done(), t2.done(), t3.done()]):
        #     await asyncio.sleep(1)

        # result = t1.result() if t1.done() else t2.result() if t2.done() else t3.result() if t3.done() else "UNINA"


        result, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        print((list(result)[0]))
        print((list(result)[0]).result())
        print(iter(result))
        print(next(iter(result)))
        first_result = next(iter(result)).result()
        print("First result:", first_result)

        # Optionally cancel remaining tasks
        for task in pending:
            task.cancel()
    return result
asyncio.run(main())
