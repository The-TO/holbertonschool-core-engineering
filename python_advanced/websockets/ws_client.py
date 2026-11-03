#!/usr/bin/env python3

import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        result = await websocket.recv()
    return result


async def main():
    result = await connect_and_send("ws://127.0.0.1:8765", "demo")
    print(result, end="")

if __name__ == "__main__":
    asyncio.run(main())
