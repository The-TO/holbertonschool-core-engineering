#!/usr/bin/env python3
"""MOdule pour valider les messages envoyer par le client"""
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Answer ERR:EMPTY for blank messages, OK:<message> otherwise."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
                await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
