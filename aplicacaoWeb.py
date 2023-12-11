from flask import Flask, render_template

app = Flask(__name__)

# Dados
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

# Rota para exibir a tabela
@app.route('/')
def index():
    # Renderiza a página HTML e passa os dados para exibição na tabela
    return render_template('index.html', data=[a, b])

if __name__ == '__main__':
    app.run(debug=True)
