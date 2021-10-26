from config import * 
from modelo import Livro 
from flask import request

@app.route("/livros")
def getLivros():
    livros = db.session.query(Livro).all()
    livros_check = [ x.json() for x in livros ]
    viewModel = jsonify(livros_check)
    viewModel.headers.add("Access-Control-Allow-Origin", "*")
    return viewModel

app.run(debug=True)