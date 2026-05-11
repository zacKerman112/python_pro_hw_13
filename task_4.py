import asyncio


async def slow_task() -> None:
    """immitating a slow task"""
    print("Task begin")
    await asyncio.sleep(10)
    print("Task complete")
    

async def task_check() -> None:
    """checking task if it takes more than 5 seconds to be complete"""
    try:
        print("waiting for the task to ba done in 5 sec time")
        await asyncio.wait_for(slow_task(), timeout=5.0)
        
    except asyncio.TimeoutError:
        print("ERROR the timeout has run out! the task takes more then 5 sec to be done!")


if __name__ == "__main__":
    asyncio.run(task_check())
            