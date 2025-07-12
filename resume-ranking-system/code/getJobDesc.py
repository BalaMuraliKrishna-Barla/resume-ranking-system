import requests
import json
import time
from tqdm import tqdm
import re

# --- Configuration ---
THREAD_IDS = {
    'Apr24': 40011496, 'Mar24': 39560867, 'Feb24': 39218209, 'Jan24': 38879979,
    'Dec23': 38495814, 'Nov23': 38115201, 'Oct23': 37785292, 'Sep23': 37381509,
    'Aug23': 37045905, 'Jul23': 36573883, 'Jun23': 36159531, 'May23': 35767227,
}
ALGOLIA_API_URL = "http://hn.algolia.com/api/v1/search_by_date" # Using the date-sorted endpoint
OUTPUT_FILE = "hacker_news_jobs.json"

def is_job_posting(text):
    """Intelligent filter to determine if a comment is a job posting."""
    if not text:
        return False
        
    score = 0
    lower_text = text.lower()
    
    hiring_keywords = ['hiring', 'we are hiring', 'we\'re hiring', 'join our team', 'looking for', 'open role']
    role_keywords = ['engineer', 'developer', 'scientist', 'designer', 'manager', 'analyst', 'architect', 'full-stack', 'backend', 'frontend', 'sre']
    location_keywords = ['remote', 'onsite', 'hybrid', 'visa', 'usd', 'eur', 'gmbh']
    
    if '|' in text.splitlines()[0]:
        score += 3
    if any(keyword in lower_text for keyword in hiring_keywords):
        score += 2
    if any(keyword in lower_text for keyword in role_keywords):
        score += 1
    if any(keyword in lower_text for keyword in location_keywords):
        score += 1
        
    return len(text) > 200 and score >= 3

def fetch_comments_for_thread(thread_id):
    """Fetches all comments for a given thread ID using the correct numeric filter."""
    all_comments = []
    page = 0
    while True:
        # *** THIS IS THE CRITICAL CHANGE ***
        # We are using numericFilters to specify the parent post ID.
        params = {
            'numericFilters': f'parent_id={thread_id}',
            'hitsPerPage': 100, # A more reasonable page size
            'page': page
        }
        try:
            response = requests.get(ALGOLIA_API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            hits = data.get('hits', [])
            if not hits:
                break
            
            all_comments.extend(hits)
            
            if page >= data.get('nbPages', 0) - 1:
                break
            
            page += 1
            time.sleep(0.3)
        except requests.exceptions.RequestException as e:
            print(f"\nError fetching page {page} for thread {thread_id}: {e}")
            break
            
    return all_comments

def main():
    """Main function to scrape and save job descriptions."""
    all_jobs = []
    job_id_counter = 0

    print("Starting data collection with the GUARANTEED method...")

    for month, thread_id in THREAD_IDS.items():
        print(f"\n--- Processing thread for {month} (ID: {thread_id}) ---")
        
        comments = fetch_comments_for_thread(thread_id)
        
        if not comments:
            print(f"Could not fetch comments for thread {thread_id}. This might be a network issue or an empty thread.")
            continue
        
        print(f"Fetched {len(comments)} total comments. Now filtering for job postings...")
        
        for comment in tqdm(comments, desc=f"Filtering {month}"):
            job_text = comment.get('comment_text')
            
            if not job_text:
                continue

            # Remove HTML tags, just in case
            job_text = re.sub('<[^<]+?>', '', job_text)

            if is_job_posting(job_text):
                job_id_counter += 1
                all_jobs.append({
                    'id': f'hn_{job_id_counter}',
                    'source': 'HackerNews',
                    'month': month,
                    'text': job_text
                })

    print(f"\n\nScraping complete. Found {len(all_jobs)} high-quality job descriptions.")

    if all_jobs:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_jobs, f, indent=4, ensure_ascii=False)
        print(f"Data successfully saved to {OUTPUT_FILE}")
    else:
        print("No job descriptions were found. Proceeding to fallback option.")

if __name__ == "__main__":
    main()