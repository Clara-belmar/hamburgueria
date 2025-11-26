from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from models import Lanche, Bebida
#cria o app flask
app = Flask(__name__)
#tenta fazer conecxão se falhar exibe a exceção
try:
    client = MongoClient("mongodb://127.0.0.1:27017")
    db=client['hamburgueria_db']
    #podemos usar uma coleção generica para todos os itens
    colecao_itens = db['itens_cardapio']
    print("conectado ao Mongo Db")
except Exception as e:
    print(f"Erro ao conectar: {e}")

@app.route('/')
def index():
    itens_banco=list(colecao_itens.find())
    return render_template ('index.html', itens=itens_banco)

@app.route('/adicionar', methods=['GET','POST'])
def adicionar():
    if request.method == 'POST':
        tipo_item = request.form['ingredientes']
        nome = request.form['nome']
        preco = float(request.form['preco'])

        if tipo_item == 'lanche':
            ingredientes = request.form['ingredientes']
            novo_item = Lanche(nome, preco, ingredientes)
        
        elif tipo_item == 'bebida':
            tamanho = request.form['tamanho']
            novo_item = Bebida(nome, preco, tamanhoMl)
        
        colecao_itens.insert_one(novo_item.convDic)

        return redirect('/')

    return render_template('adicionar.html')

if __name__ == '__main__':
    app.run(debug=True)