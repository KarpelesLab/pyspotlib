#!/usr/bin/env python3
"""Basic usage example for pyspotlib."""

import asyncio
from pyspotlib import new_client


async def main():
    # Create and start a client
    client = await new_client()

    # Wait for connection to be online
    print("Connecting to Spot network...")
    await client.wait_online(timeout=30)
    print(f"Connected! Target ID: {client.target_id}")

    # Get server time
    print("\n--- Server Time ---")
    ts = await client.get_time()
    print(f"Server time: {ts}")

    # Store and fetch a blob
    print("\n--- Blob Storage ---")
    test_data = b"Hello from Python!"
    await client.store_blob("example_key", test_data)
    print(f"Stored: {test_data}")

    fetched = await client.fetch_blob("example_key")
    print(f"Fetched: {fetched}")

    # Clean up
    await client.close()
    print("\nDone!")


if __name__ == "__main__":
    asyncio.run(main())
