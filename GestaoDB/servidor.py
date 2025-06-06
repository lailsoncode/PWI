#importar a classe Flask
from flask import *

import gestaoDB

#instanciar o servidor Flask
app = Flask(__name__)

#criar banco / tabela
gestaoDB.criarTabela()

usuarios = []

#app.register_blueprint(home_route)

#rota padrão (página principal)
@app.route("/")
def principal():
    return render_template("index.html")

#rota para direcionar para Página de Cadastro
@app.route("/paginaCadastro")
def paginaCadastro():
    return render_template("cadastro.html")

#rota para receber os dados do usuário e cadastrar novo usuário na lista
@app.route("/cadastrarUsuario", methods=['POST'])
def cadastrarUsuario():
    nome = request.form.get('nomeUsuario')
    login = request.form.get('loginUsuario')
    senha = str(request.form.get('senhaUsuario'))
    if(gestaoDB.verificarUsuario(login)==False):
        gestaoDB.inserirUsuario(nome, login, senha)
        mensagem="usuário cadastrado com sucesso"
        return render_template("resultado.html", mensagem=mensagem)
    else:
        mensagem="usuário já existe"
        return render_template("resultado.html", mensagem=mensagem)

#rota para receber login e senha e fazer a autenticação (login)
@app.route("/autenticarUsuario", methods=['POST'])
def autenticar():
    login = request.form.get("loginUsuario")
    senha = str(request.form.get("senhaUsuario"))
    
    logado=gestaoDB.login(login, senha)

    if(logado==True):
        mensagem="usuário logado com sucesso"
        return render_template("resultado.html", mensagem=mensagem)
    else:    
        mensagem="usuario ou senha incorreto"
        return render_template("resultado.html", mensagem=mensagem)

@app.route("/listarUsuarios")
def listarUsuarios():
    #return render_template("lista.html", lista=lista_usuarios)
    lista_usuariosDB = gestaoDB.listarUsuarios()
    return render_template("listar.html", lista=lista_usuariosDB)

@app.route("/paginaRecuperarSenha")
def paginaRecuperar():
    return render_template("recuperar.html")

@app.route("/recuperarSenha", methods=['POST'])
def recuperarSenha():
    login = request.form.get("loginUsuario")
   
    encontrado=False

    if(gestaoDB.verificarUsuario(login)==True):
        encontrado=True

    if(encontrado==True):
        senha = str(gestaoDB.recuperarSenhaBD(login))
        mensagem="sua senha: "+senha
        return render_template("resultado.html", mensagem=mensagem)
    else:    
        mensagem="usuario nao encontrado"
        return render_template("resultado.html", mensagem=mensagem)
    
@app.route("/paginaAlterarSenha")
def paginaAlterar():
    return render_template("alterar.html")

@app.route("/alterarSenha", methods=['POST'])
def alterarSenha():
    login = request.form.get("loginUsuario")
    senha = str(request.form.get("senhaUsuario"))
    
    if(gestaoDB.verificarUsuario(login)==True):
        gestaoDB.alterarSenhaBD(login, senha)
        mensagem="senha alterada com sucesso"
        return render_template("resultado.html", mensagem=mensagem)
    else:    
        mensagem="usuario nao encontrado"
        return render_template("resultado.html", mensagem=mensagem)
    
#executar o servidor Flask
app.run(debug=True)