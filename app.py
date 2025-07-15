from flask import Flask, request, jsonify, render_template
from openai import AzureOpenAI

app = Flask(__name__)

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://frun1-mcodqqee-eastus2.cognitiveservices.azure.com/",
    api_key="YOUR_API_KEY"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=1024,
        model="nickbot"
    )

    return jsonify({"response": response.choices[0].message.content})