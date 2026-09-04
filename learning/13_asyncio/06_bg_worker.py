import asyncio
import threading
import time

def background_worker(item):
    while True:
        time.sleep(1)  # Simulate a delay in checking stock
        print(f"{item} is in stock!")

async def fetch_orders():
    print("Fetching orders...")
    await asyncio.sleep(3)  # Simulate a delay in fetching orders
    return ["Masala chai", "Green tea", "Black coffee"]

threading.Thread(target=background_worker, args=("Masala chai",), daemon=True).start()

asyncio.run(fetch_orders())
    
