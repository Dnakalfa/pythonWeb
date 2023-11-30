import pandas as pd
from flask import Flask, jsonify
import random as r
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

a = {
    "Nome": "Umberto",
    "Sobrenome": "Alves",
    "Idade": 42,
    "Formacao": "Análise e Desenvolvimento de Software"
}
b = {
    "Nome": "Carol",
    "Sobrenome": "Alves",
    "Idade": 37,
    "Formacao": "Direito"
}

@app.route("/")
def home():
    return "<marquee><h3> Tabela com informações gerais </h3></marquee>"

@app.route("/input")
def input_():
    return jsonify(a)

@app.route('/output', methods=['GET', 'POST'])
def pred_json():
    pred = r.choice(["positive", "negative"])
    nd = b.copy()
    nd["prediction"] = pred
    return jsonify(nd)

# Obtendo a URL pública do ngrok
ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)

# Aplicando o loop de eventos do Nest_asyncio
nest_asyncio.apply()

# Configurando o servidor Uvicorn com o app Flask
uvicorn.run(app, host='127.0.0.1', port=8000)
