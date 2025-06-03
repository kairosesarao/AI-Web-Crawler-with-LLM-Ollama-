from flask import Flask, render_template, request
from crawler_main import crawl
from analyze import analyze_article

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        keyword = request.form["keyword"]
        crawled = crawl(keyword)
        for article in crawled:
            analysis = analyze_article(article["title"], article["content"])
            article["analysis"] = analysis
            results.append(article)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
