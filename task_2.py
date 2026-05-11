import asyncio
import aiohttp


async def fetch_content(url: str) -> Exception:
    """a function for fetching data"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as responce:
                responce.raise_for_status()
                return await responce.text()
    
    except aiohttp.ClientError as e:
        return f"client error for {url}: {e}"
    except asyncio.TimeoutError:
        return f"the {url} is out of time" 
    except Exception as e:
        return f"some unexpected error for {url}: {e}"
           

async def fetch_all(urls: list) -> list:
    tasks = [fetch_content(url) for url in urls]
    
    results = await asyncio.gather(*tasks)
    return results


async def main() -> None:
    urls_to_load = [
        "https://www.google.com",
        "https://www.python.org",
        "https://api.github.com",
        "https://non-existent-website-123.com"
    ]
    
    print("download begin...")
    
    pages = await fetch_all(urls_to_load)
    
    for url, content in zip(urls_to_load, pages):
        print("\nURL: {url}")
        print(f"content: {content[:100]}...")
        
if __name__ == "__main__":
    asyncio.run(main())        