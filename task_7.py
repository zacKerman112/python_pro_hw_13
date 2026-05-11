import asyncio
import aiohttp
import requests
import time
from concurrent.futures import ThreadPoolExecutor
from typing import List, Any, Callable, Coroutine

URL: str = "https://www.google.com"
N: int = 20


def synchronous() -> List[requests.Response]:
    """Execute HTTP requests sequentially."""
    return [requests.get(URL) for _ in range(N)]


def threaded() -> List[requests.Response]:
    """Execute HTTP requests concurrently using a thread pool."""
    with ThreadPoolExecutor() as executor:
        return list(executor.map(lambda u: requests.get(u), [URL] * N))


async def async_run() -> List[aiohttp.ClientResponse]:
    """Execute HTTP requests concurrently using asyncio and aiohttp."""
    async with aiohttp.ClientSession() as s:
        return await asyncio.gather(*(s.get(URL) for _ in range(N)))


def benchmark(name: str, func: Callable[..., Any], is_async: bool = False) -> None:
    """Measure and print the execution time of a given function."""
    start = time.time()
    if is_async:
        asyncio.run(func())
    else:
        func()
    print(f"{name:10}: {time.time() - start:.2f}sec")


if __name__ == "__main__":
    benchmark("Sync", synchronous)
    benchmark("Threads", threaded)
    benchmark("Async", async_run, True)