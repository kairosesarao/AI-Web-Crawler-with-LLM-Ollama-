import requests

def analyze_article(title, content):
    prompt = f"""
    Analyze this article:

    Title: {title}
    Content: {content}

    Instructions:
    1. Summarize in 3 lines
    2. Categorize it (e.g. tech, finance, climate)
    3. Provide sentiment (Positive/Negative/Neutral)
    4. Suggest one useful insight
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        data = response.json()
        return data.get("response", "⚠️ No response from Ollama.")
    except Exception as e:
        return f"⚠️ Error from Ollama: {str(e)}"
