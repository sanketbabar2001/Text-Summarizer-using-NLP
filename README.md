# Text-Summarizer-using-NLP

This project is a Text Summarization application that uses Natural Language Processing (NLP) techniques to generate concise summaries of longer texts.

# 1. Create a virtual environment and activate it :
python -m venv myenv
myenv\Scripts\activate

# 2. Install the project dependencies:
pip install -r requirements.txt

# 3. To train the summarization model, run the following command :
python main.py

# Note:
This will initiate the data ingestion, validation, transformation, model training, and evaluation stages. It may take some time to complete, depending on your hardware and configuration.

# 4. To start the Flask web application for text summarization, use the following command :
python app.py

The web app will be accessible at http://127.0.0.1:8080 in your web browser.

# 5. Usage
Visit the web application at http://127.0.0.1:8080.
Enter the text you want to summarize in the provided textarea.
Click the "Summarize" button to generate a summary.
The summarized text will be displayed below the input.