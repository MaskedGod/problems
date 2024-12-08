from datetime import datetime
import asyncio
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler


def tick():
    print(f"Tick! The time is: {datetime.now()}")


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(tick, "interval", seconds=3)
    scheduler.start()
    print("Press Ctrl+{0} to exit".format("Break" if os.name == "nt" else "C"))
    while True:
        await asyncio.sleep(1000)


if __name__ == "__main__":
    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass