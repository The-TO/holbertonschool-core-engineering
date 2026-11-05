#!/usr/bin/env python3

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

clients = set()


async def broadcast(message: str) -> None:
    for client in list(clients):
        try:
            await client.send(message)
        except ConnectionClosed:
            clients.discard(client)


async def echo(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            if message.isspace() or not message:
                await websocket.send('ERR:EMPTY')
            else:
                await broadcast(f'B:{message}')
    except ConnectionClosed:
        pass
    finally:
        clients.discard(websocket)


async def main():
    async with serve(echo, '127.0.0.1', 8765):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
