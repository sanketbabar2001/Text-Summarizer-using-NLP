from flask import Flask, render_template, request, jsonify
from textSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        text = request.form['text']
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return render_template('index.html', summary=summary)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)

