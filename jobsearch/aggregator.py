
from .remotive import fetch_remotive_jobs
from .jsearch import fetch_jsearch_keyword_jobs

async def fetch_combined_jobs(keyword: str, location: str = None):
    remotive_jobs = await fetch_remotive_jobs(keyword, location)
    jsearch_jobs = await fetch_jsearch_keyword_jobs(keyword + (f" {location}" if location else ""))
    return (remotive_jobs + jsearch_jobs)[:10]
