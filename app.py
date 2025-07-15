from flask import Flask, request, jsonify, render_template
from openai import AzureOpenAI

app = Flask(__name__)

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://nickbot-hxhfhga5d9hfeqdr.eastus2-01.azurewebsites.net/chat",
    api_key="BHJTlXPFMUeoPyKyiWTuyjD7Yqr2CIgYamSrcl369gec6FeeprxiJQQJ99BGACHYHv6XJ3w3AAAAACOGvJtk"
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