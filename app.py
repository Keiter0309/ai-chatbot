from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

# Configure the AI service with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/ask-gemini', methods=['POST'])
def ask_gemini():
    data = request.get_json()
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(data['text'])
    return jsonify({'response': response.text})

if __name__ == "__main__":
    app.run(debug=True)

