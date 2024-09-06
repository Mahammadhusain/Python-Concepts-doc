# ==========================================================================
  # Sync
# ==========================================================================

# import time
# def task(name):
#     print(f"Task {name} started")
#     time.sleep(2)  # Simulating a time-consuming task
#     print(f"Task {name} finished")

# def main():
#     task("A")
#     task("B")
#     task("C")

# if __name__ == "__main__":
#     main()

# ==========================================================================
  # async
# ==========================================================================

import asyncio

async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    print(f"Task {name} finished")

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C"),
        task("D"),
    )

if __name__ == "__main__":
    asyncio.run(main())
