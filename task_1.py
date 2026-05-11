import asyncio
import random


async def download_page(url: str) -> None:
    """downloading the pages"""
    load_time = random.uniform(1, 5)
    print(f"downloading a page from {url}")
    await asyncio.sleep(load_time)
    print(f"the pade from {url} has been downloaded in {load_time:.2f} sec.")
    

async def main(urls: list) -> None:
    """using the functionality of download_page() and putting it to use"""
    print(f"downloading {len(urls)} pages at the same time")
    
    tasks = []
    for url in urls:
        tasks.append(download_page(url))
        
        await asyncio.gather(*tasks)
        print("all the pages downloaded")


if __name__ == "__main__":
    list_of_urls = [
        "https://google.com",
        "https://github.com",
        "https://python.org",
        "https://stackoverflow.com"
    ]     
    
    asyncio.run(main(list_of_urls))
        