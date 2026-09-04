import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stocks(item):
    print(f"Checking stock for {item}...")
    time.sleep(2)  # Simulate a delay in checking stock
    return f"{item} is in stock!"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, check_stocks, "Masala chai")
        print(result)

asyncio.run(main())