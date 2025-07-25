
# 🔍 Job Search Aggregator API Wrapper

A Python wrapper that combines results from Remotive and JSearch APIs to fetch remote or keyword-based job listings. Ideal for job bots, career platforms, and automation projects.

## 🚀 Features
- Fetch jobs by keyword, category, or location
- Integrates Remotive and JSearch (via RapidAPI)
- Simple async interface
- Filter or combine multiple sources

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🔧 Usage

```python
from jobsearch.aggregator import fetch_combined_jobs

results = await fetch_combined_jobs("software developer", location="Remote")
for job in results:
    print(job["title"], job["company"], job["url"])
```

## 📁 API Sources
- [Remotive API](https://remotive.io/api)
- [JSearch API on RapidAPI](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch)

## ✅ To-Do
- Add pagination support
- Add error handling and retries
- Add unit tests

---

👨‍💻 Made with ❤️ by Lasisi Ibrahim
