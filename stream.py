import os
import asyncio

class Subscriber:
    def __init__(self, id):
        self.id=id
    
    
class Pub:
    def __init__(self):
        self.sus = {}
        self.value = 0
    
    def subscribe(self, ber:Subscriber, cb):
        self.sus[ber.id] = cb

        return { 
            "unsubscribe": lambda: self.unsubscribe(ber.id)
        }
    
    def emit(self, text):
        for id, cb in self.sus.items():
            cb(text)
    def unsubscribe(self, id):
        del self.sus[id]


    async def stream(self):
        while True:
            self.value += 1
            await asyncio.sleep(1)
            self.emit(self.value)


async def main():
    publisher = Pub()
    sus = Subscriber(1)
    subscribed1 = publisher.subscribe(sus, print)
    sus = Subscriber(2)
    subscribed2 = publisher.subscribe(sus, lambda text: print(text, ": for 2"))
    task = asyncio.create_task(publisher.stream())
    # collect = set([task])
    # await asyncio.sleep(5)

    # print(subscribed1["unsubscribe"]())
    await task

asyncio.run(main())