from flask import Flask, jsonify
import random as r
import nest_asyncio
import uvicorn

app = Flask(__name__)

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

# Aplicando o loop de eventos do Nest_asyncio
nest_asyncio.apply()

# Configurando o servidor Uvicorn com o app Flask
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
