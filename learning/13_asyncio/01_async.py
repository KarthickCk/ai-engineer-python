import asyncio

async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)  # Simulate time taken to brew chai
    print("Chai is ready!")

asyncio.run(brew_chai())