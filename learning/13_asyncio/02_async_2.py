import asyncio

async def brew_chai(name):
    print(f"Brewing chai for {name}...")
    await asyncio.sleep(2)  # Simulate time taken to brew chai
    print(f"Chai is ready for {name}!")

async def main():
    await asyncio.gather(
        brew_chai("Alice"),
        brew_chai("Bob"),
        brew_chai("Charlie")
    )

asyncio.run(main())