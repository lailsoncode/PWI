# Criar uma aplicação Web para gestão de usuários, com a seguintes funcionalidades:
# Cadastrar novo usuário; Listar usuários cadastrados; Realizar login;
# e, Excluir usuário. Utilizar Python + Flask para criar o backend da aplicação.

#importar a classe Flask
from flask import *

#instanciar o servidor Flask
app = Flask(__name__)

#criar variável global (lista de usuários)
listaUsuarios = []

#rota padrão (ir para página principal)
@app.route("/")
def principal():
    return render_template("index.html")

#rota para direcionar para página de cadastro
@app.route("/paginaCadastro")
def paginaCadastro():
    return render_template("cadastro.html")

#rota para alterar nome login
@app.route("/paginaAlterar")
def paginaAlterar():
    return render_template("alterar.html")

#rota para direcionar para página de cadastro
@app.route("/paginaLista")
def paginalistar():
    return render_template("listar.html", lista=listaUsuarios) #precisava passar a variável

#rota para direcionar para página de recuperar senha
@app.route("/paginaRecuperar")
def paginaRecuperar():
    return render_template("recuperar.html")


@app.route("/cadastrarUsuario", methods=["POST"])
def cadastrar():
    
    nome = request.form.get("nomeUsuario")
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")
    
    listaUsuarios.append([nome, login, senha])
    mensagem="Usuário Cadastrado com Sucesso"
    return render_template("resultado.html", mensagem=mensagem)


#criar uma rota para verificar se o usuário está na lista de convidados
@app.route("/verificarUsuario", methods=['POST'])
def verificar():
    nome = request.form.get("nomeUsuario")
    if(nome in listaUsuarios):
        mensagem="você está convidado"
        return render_template("resultado.html", mensagem=mensagem)
    else:
        mensagem="você NÃO está convidado"
        return render_template("resultado.html", mensagem=mensagem)

#criar uma rota para listar os usuários cadastrados
@app.route("/listarConvidados")
def listarConvidados():
    return render_template("listar.html", lista=listaUsuarios)

#criar uma rota para listar os usuários cadastrados
@app.route("/excluirUsuario", methods=["POST"])
def excluir():
    nome = request.form.get("nomeUsuario")
    for i in range(len(listaUsuarios)):
        if listaUsuarios[i][0] == nome:
            del listaUsuarios[i]
            mensagem="Usuário Excluído com Sucesso"
            return render_template("resultado.html", mensagem=mensagem)
    mensagem="Usuário não encontrado"
    return render_template("resultado.html", mensagem=mensagem)

#criar uma rota para realizar o login
@app.route("/login", methods=["POST"])
def login():
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")
    
    for usuario in listaUsuarios:
        if usuario[1] == login and usuario[2] == senha:
            mensagem="Login realizado com sucesso"
            return render_template("resultado.html", mensagem=mensagem)
    
    mensagem="Login ou senha inválidos"
    return render_template("resultado.html", mensagem=mensagem)

#criar funcao para recuperar senha
@app.route("/recuperarSenha", methods=["POST"])
def recuperarSenha():
    login = request.form.get("loginUsuario")
    
    for usuario in listaUsuarios:
        if usuario[1] == login:
            mensagem = f"Sua senha é: {usuario[2]}"
            break
    else:
        mensagem = "Login não encontrado."

    return render_template("resultado.html", mensagem=mensagem)

#criar funcao para alterar login e senha
@app.route("/alterarLogin", methods=["POST"])
def alterarLogin():
    nome = request.form.get("nomeUsuario")
    novo_login = request.form.get("novoLogin")

    for usuario in listaUsuarios:
        if usuario[0] == nome:
            usuario[1] = novo_login
            mensagem = "Login alterado com sucesso."
            break
    else:
        mensagem = "Usuário não encontrado."

    return render_template("resultado.html", mensagem=mensagem)

#executar o servidor Flask
app.run(debug=True)