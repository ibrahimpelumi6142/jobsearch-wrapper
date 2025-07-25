
import httpx
import os

JSEARCH_API_KEY = os.getenv("JSEARCH_API_KEY")

async def fetch_jsearch_keyword_jobs(query):
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": JSEARCH_API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {"query": query, "num_pages": 1}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        data = response.json()
        jobs = [
            {
                "title": job["job_title"],
                "company": job["employer_name"],
                "location": job.get("job_city") or "N/A",
                "url": job["job_apply_link"],
            }
            for job in data.get("data", [])
        ]
        return jobs
