import asyncio
import aiohttp
from typing import List


async def download_image(session: aiohttp.ClientSession, url: str, name: str) -> None:
    """Download an image from a URL and save it to the local disk."""
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.read()
            with open(name, "wb") as file:
                file.write(content)
            print(f"saved: {name}")


async def main() -> None:
    """Coordinate the concurrent downloading of multiple images."""
    urls: List[str] = [
        f"https://via.placeholder.com/600/{hex_code}" 
        for hex_code in ["92c952", "771796", "24f355"]
    ]              
    
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *(download_image(session, url, f"img_{i}.png") for i, url in enumerate(urls))
        )


if __name__ == "__main__":
    asyncio.run(main())