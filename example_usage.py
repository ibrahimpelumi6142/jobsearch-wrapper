
import asyncio
from jobsearch.aggregator import fetch_combined_jobs

async def main():
    jobs = await fetch_combined_jobs("python developer", location="remote")
    for job in jobs:
        print(f"{job['title']} at {job['company']} - {job['location']}")
        print(job['url'], "\n")

if __name__ == "__main__":
    asyncio.run(main())
