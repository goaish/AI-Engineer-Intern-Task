#  LLM-Based Review Scraper & Sentiment Analyzer

##  Project Overview

This project is an end-to-end Python application that demonstrates the integration of **web scraping, data preprocessing, and Large Language Model (LLM) interaction**.

The system takes a product webpage URL as input, extracts textual data (treated as reviews/descriptions), processes the data, and generates **sentiment summaries using an OpenAI-compatible API**. The final output is stored in a structured format for analysis.

---

##  Objective

The objective of this project is to:

- Scrape product-related textual data from a web page  
- Extract useful information such as text and ratings  
- Preprocess raw text to make it suitable for LLM input  
- Use an LLM API to generate sentiment summaries  
- Store results in a structured format (CSV)  
- Handle common issues like API failures and rate limits  

---

##  Chosen Product URL

Due to anti-scraping protections on major e-commerce platforms (e.g., Amazon), the following publicly available test site was used:

 https://webscraper.io/test-sites/e-commerce/static/computers/laptops

This site provides a stable HTML structure, allowing reliable scraping for demonstration purposes.

---

##  System Architecture
            ┌────────────────────┐
            │   Input URL        │
            └─────────┬──────────┘
                      │
                      ▼
            ┌────────────────────┐
            │  Web Scraper       │
            │ (Requests + BS4)   │
            └─────────┬──────────┘
                      │
                      ▼
            ┌────────────────────┐
            │ Data Extraction    │
            │ (Text, Rating)     │
            └─────────┬──────────┘
                      │
                      ▼
            ┌────────────────────┐
            │ Preprocessing      │
            │ - Clean text       │
            │ - Remove noise     │
            │ - Truncate input   │
            └─────────┬──────────┘
                      │
                      ▼
            ┌────────────────────┐
            │ LLM API Call       │
            │ (OpenAI GPT Model) │
            └─────────┬──────────┘
                      │
                      ▼
            ┌────────────────────┐
            │ Sentiment Output   │
            │ (Summary + Reason) │
            └─────────┬──────────┘
                      │
                      ▼
            ┌────────────────────┐
            │ CSV Storage        │
            │ (Structured Data)  │
            └────────────────────┘
            
---

##  Features

-  Web scraping using BeautifulSoup
-  Text preprocessing (cleaning + truncation)
-  LLM-based sentiment analysis
-  Structured CSV output
-  Error handling for:
  - Network issues
  - API failures
  - Rate limits
-  Delay mechanism to prevent API throttling

---

##  Tech Stack

| Component        | Technology Used        |
|----------------|----------------------|
| Programming     | Python               |
| Web Scraping    | Requests, BeautifulSoup |
| Data Handling   | Pandas               |
| LLM API         | OpenAI API           |
| Environment     | python-dotenv        |

---

##  Installation & Setup

### 1. Clone the Repository
git clone <your-repo-link>
cd llm-review-scraper


### 2. Install Dependencies
pip install -r requirements.txt


### 3. Setup Environment Variables
Create a `.env` file in the root directory:
OPENAI_API_KEY=your_api_key_here

##  How to Run the Application
Run the following command:

When prompted, enter the product URL: https://webscraper.io/test-sites/e-commerce/static/computers/laptops


---

##  Workflow Explanation

1. The user provides a product URL  
2. The scraper fetches and parses the HTML content  
3. Relevant text and metadata are extracted  
4. Text is cleaned and truncated for LLM compatibility  
5. Each entry is sent to the LLM API  
6. The LLM generates a sentiment summary  
7. Results are stored in a CSV file  

---

##  Output Format

The application generates an `output.csv` file with the following columns:

| Column   | Description |
|---------|------------|
| text     | Extracted textual content |
| rating   | Extracted rating value |
| author   | Placeholder (if unavailable) |
| date     | Placeholder (if unavailable) |
| summary  | LLM-generated sentiment |

---

##  Design Decisions

### 1. Modular Architecture
Each stage (scraping, preprocessing, LLM interaction) is separated for scalability and maintainability.

### 2. Token Management
Long texts are truncated (`text[:1000]`) to stay within model token limits.

### 3. Rate Limiting Handling
A delay (`time.sleep(1)`) is introduced between API calls to avoid hitting rate limits.

### 4. Error Handling
- Network errors handled using try-except blocks  
- API errors captured and logged  
- Fallback responses returned when failures occur  

### 5. Website Selection Strategy
Amazon and similar platforms block automated scraping. Therefore, a test website was used to ensure reliability while demonstrating the same pipeline.

---

##  Limitations

- Scraper depends on specific HTML structure  
- Only a single page is scraped (no pagination)  
- Limited metadata availability  
- API latency due to sequential calls  
- Results depend on LLM output quality  

---

##  Future Improvements

- Implement pagination to scrape multiple pages  
- Use async/batch LLM calls for performance  
- Add support for multiple websites dynamically  
- Build a UI dashboard (e.g., Streamlit)  
- Store results in a database instead of CSV  
- Improve preprocessing (stopword removal, normalization)  

---

##  Demo Video

https://www.loom.com/share/3f55750330aa4af6aecd1a01352a4cca

---

##  Conclusion

This project demonstrates a real-world pipeline combining **web scraping and LLM-based natural language processing**. It highlights practical skills in API integration, data processing, and system design, making it highly relevant for AI/ML engineering roles.

---
