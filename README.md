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

## 📸 Screenshot for showcasing the working project

Below is the screenshots of the assignment for reeference when analyzing "climate change":

![Screenshot of Ollama Terminal running](https://github.com/kairosesarao/AI-Web-Crawler-with-LLM-Ollama-/blob/main/Ollama%20Terminal%20running.png?raw=true)
![Screenshot of Terminal Running Flask Pic -1](https://github.com/kairosesarao/AI-Web-Crawler-with-LLM-Ollama-/blob/main/Terminal%20Running%20Flask%20Pic%20-1.png?raw=true)
![Screenshot of Terminal running Flask Pic -2](https://github.com/kairosesarao/AI-Web-Crawler-with-LLM-Ollama-/blob/main/Terminal%20running%20Flask%20Pic%20-2.png?raw=true)
![Screenshot of Web Interface (Flask Page) in Browser](https://github.com/kairosesarao/AI-Web-Crawler-with-LLM-Ollama-/blob/main/Web%20Interface%20(Flask%20Page)%20in%20Browser.png?raw=true)
![Screenshot of JSON file Image](https://github.com/kairosesarao/AI-Web-Crawler-with-LLM-Ollama-/blob/main/JSON%20file%20Image.png?raw=true)


