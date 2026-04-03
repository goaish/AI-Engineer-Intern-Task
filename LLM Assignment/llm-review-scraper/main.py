import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# LOAD API KEY
# -----------------------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# SCRAPE REVIEWS (Amazon-like)
# -----------------------------
def scrape_reviews(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    reviews = []

    items = soup.find_all("div", class_="thumbnail")

    for item in items:
        try:
            title = item.find("a", class_="title").get_text(strip=True)
            description = item.find("p", class_="description").get_text(strip=True)
            rating = item.find("div", class_="ratings").find_all("span", class_="glyphicon-star")
            rating = len(rating)

            reviews.append({
                "text": description,
                "rating": rating,
                "author": "Anonymous",
                "date": "N/A"
            })
        except:
            continue

    return reviews

# -----------------------------
# CLEAN TEXT
# -----------------------------
def clean_text(text):
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    return text.strip()

# -----------------------------
# LLM SUMMARIZATION / SENTIMENT
# -----------------------------
def summarize_review(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Give sentiment (Positive/Negative/Neutral) + short reason in one line."
                },
                {
                    "role": "user",
                    "content": text[:1000]  # truncate long reviews
                }
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# -----------------------------
# MAIN PIPELINE
# -----------------------------
def process(url):
    print("🔄 Scraping reviews...")
    data = scrape_reviews(url)

    if not data:
        print("❌ No reviews found. Try another URL.")
        return

    print(f"✅ Found {len(data)} reviews")

    results = []

    for i, review in enumerate(data):
        print(f"🤖 Processing review {i+1}/{len(data)}...")

        cleaned = clean_text(review["text"])
        summary = summarize_review(cleaned)

        results.append({
            "text": review["text"],
            "rating": review["rating"],
            "author": review["author"],
            "date": review["date"],
            "summary": summary
        })

        time.sleep(1)  # avoid rate limits

    df = pd.DataFrame(results)
    df.to_csv("output.csv", index=False)

    print("\n🎉 Done! Data saved to output.csv")

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    url = input("🔗 Enter product review URL: ").strip()
    process(url)