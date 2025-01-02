# filepath: /E:/Coding/Oqila-1/backend/app.py
from flask import Flask, request, jsonify
from openai_api.api_handler import OpenAIHandler
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()
app = Flask(__name__)
openai_handler = OpenAIHandler(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    response = openai_handler.generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)