
import httpx

async def fetch_remotive_jobs(category_or_keyword, location=None):
    async with httpx.AsyncClient() as client:
        url = "https://remotive.io/api/remote-jobs"
        response = await client.get(url)
        data = response.json()
        keyword = category_or_keyword.lower()
        jobs = [
            {
                "title": job["title"],
                "company": job["company_name"],
                "location": job["candidate_required_location"],
                "url": job["url"],
            }
            for job in data.get("jobs", [])
            if keyword in job["title"].lower()
        ]
        return jobs
