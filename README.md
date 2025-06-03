# 🕸️ AI-Powered Web Crawler with Local LLM (Ollama)

## Overview
This project is a beginner-friendly AI web crawler built with Python (requests + BeautifulSoup), Flask, and a local LLM using Ollama. It crawls articles based on a keyword, analyzes them using a local model like LLaMA3, and displays results on a simple web dashboard.

## Features
- Keyword-based crawling (via Bing + BeautifulSoup)
- Article extraction (title + paragraph content)
- Local LLM (Ollama) analysis: summary, category, sentiment, and insight
- Simple web UI (Flask + Jinja2)

## Setup

### 1. Install requirements

```bash
pip install flask requests beautifulsoup4
```

### 2. Install and run Ollama

- Download from: https://ollama.com
- In terminal, run:
```bash
ollama run llama3
```

### 3. Start the Flask app

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Credits
This project was created by me **Kairose Sarao** as part of an internship assignment to demonstrate practical skills in AI, web crawling, and full-stack development.


## 📸 Screenshot

![App Screenshot](screenshot.png)


