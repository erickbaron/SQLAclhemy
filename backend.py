from config import *
from modelo import Produto

@app.route("/")
def inicio():
    return 'Sistema de cadastro de produtos. '+\
        '<a href="/getProdutos">Listar</a>'

@app.route("/getProdutos")
def getProdutos():
    produtos = db.session.query(Produto).all()
    produtosJson = [ x.json() for x in produtos ]
    resposta = jsonify(produtosJson)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)  