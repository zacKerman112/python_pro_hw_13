import asyncio
import random
from typing import NoReturn


async def produser(queue: asyncio.Queue[str]) -> None:
    """Generate tasks and add them to the queue."""
    for i in range(1, 6):
        print(f"Producer: making task number {i}")
        await asyncio.sleep(1)
        await queue.put(f"task number {i}")
        print(f"Producer: added task number {i} into the queue")
    
    print("Producer: all the tasks added")


async def consumer(name: str, queue: asyncio.Queue[str]) -> NoReturn:
    """Continuously process tasks from the queue."""
    while True:
        task = await queue.get()
        
        print(f"Consumer {name}: began work with {task}")
        await asyncio.sleep(2)
        print(f"Consumer {name}: ended {task}")
        
        queue.task_done()
        
        
async def main() -> None:
    """Initialize the queue and manage producer/consumer lifecycle."""
    queue: asyncio.Queue[str] = asyncio.Queue()
    
    producer_task = asyncio.create_task(produser(queue))
    
    consumers = [
        asyncio.create_task(consumer("A", queue)),
        asyncio.create_task(consumer("B", queue))
    ]        
    
    await producer_task
    
    await queue.join()
    
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    asyncio.run(main())