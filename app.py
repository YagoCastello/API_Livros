from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id':1,
     'titulo':'O Senhor dos Anéis - A Sociedade do Anel',
     'autor':'J.R.R Tolkien'},
     {
         'id':2,
         'título':'Harry Potter e a Pedra Filosofal',
         'autor':'J.K Howling'
     },
     {
         'id':3,
         'título':'James Clear',
         'autor':'Hábitos Atômicos'
     },
] 

# Consultar(todos)
@app.route('/livros')
def obter_livros():
    return jsonify(livros)
# Consultar(id)
# Ediitar
# Excluir
app.run(port=5000,host='localhost',debug=True)
