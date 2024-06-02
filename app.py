from flask import Flask, render_template, jsonify
import twitter_scraper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    result = twitter_scraper.fetch_trending_topics()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
