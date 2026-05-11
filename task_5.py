from aiohttp import web
import asyncio


async def handle_hello(request: web.Request) -> web.Response:
    """Respond with a simple hello message."""
    return web.Response(text="Hello")


async def handle_slow(request: web.Request) -> web.Response:
    """Simulate a long-running asynchronous operation."""
    print("got the request on /slow, beginning the processing...")
    await asyncio.sleep(5)
    return web.Response(text="operation complete")


async def main() -> None:
    """Set up and start the web server application."""
    app = web.Application()
    
    app.add_routes([
        web.get('/', handle_hello),
        web.get('/slow', handle_slow)
    ])
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    
    print("server run: http://localhost:8080")
    await site.start()

    await asyncio.Event().wait()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nserver stopped")