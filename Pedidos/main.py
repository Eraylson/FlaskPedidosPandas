from flask import Flask, render_template, request, redirect, url_for
from dados.tabela import abrir_tabela, adicionar_pedido, deletar_pedido, salvar_tabela, buscar_pedido_id, editar_pedido
app = Flask(__name__)

@app.route("/")
def index():
    nome_tabela = 'cliente'
    tabela = abrir_tabela(nome_tabela)
    return render_template("index.html", pedidos = tabela)


@app.route("/pedido/", methods=['GET', 'POST'])
def pedido():
    if request.method == 'GET':
        return render_template("pedido.html")
    else:
        nome = request.form['nome']
        endereco = request.form['endereco']
        pedido = request.form['pedido']
        adicionar_pedido(nome, endereco, pedido, 'cliente')
        return redirect(url_for('index'))

@app.route("/excluir/<int:id>")
def excluir(id):

    nome_tabela = 'cliente'
    tabela = abrir_tabela(nome_tabela)
    tabela = deletar_pedido(id, tabela)
    salvar_tabela(nome_tabela, tabela)
    return redirect(url_for('index'))

@app.route("/editar/<int:id>", methods=['GET', 'POST'])
def editar(id):
    nome_tabela = 'cliente'
    tabela = abrir_tabela(nome_tabela)

    if request.method == 'GET':
        pedido = buscar_pedido_id(id, tabela)
        return render_template("pedido_edit.html", pedido = pedido)
    else:
        nome = request.form['nome']
        endereco = request.form['endereco']
        pedido = request.form['pedido']
        tabela = editar_pedido(id, tabela, nome, endereco, pedido)
        salvar_tabela(nome_tabela, tabela)
        return redirect(url_for('index'))



if __name__ == '__main__':

    app.run(debug=True)