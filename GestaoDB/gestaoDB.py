import sqlite3 as sqlite

def criarTabela():
    conn = sqlite.connect('gestaoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            login TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inserirUsuario(nome, login, senha):
    conn = sqlite.connect('gestaoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, login, senha) VALUES (?, ?, ?)
    ''', (nome, login, senha))
    conn.commit()
    conn.close()

def listarUsuarios():
    conn = sqlite.connect('gestaoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios order by id desc')
    dados = cursor.fetchall()
    usuarios = []
    for dado in dados:
        usuarios.append(dado)
    conn.close()
    return usuarios

def login(login, senha):
    conn = sqlite.connect('gestaoDB.sqlite')
    cursor = conn.cursor()
    #cursor.execute(f"SELECT * FROM usuarios WHERE login='{login}' and senha='{senha}'")
    cursor.execute("SELECT * FROM usuarios WHERE login=? and senha=?", (login, senha))
    dados = cursor.fetchall()
    conn.close()
    if len(dados) > 0:
        return True
    else:
        return False

def verificarUsuario(login):
    conn = sqlite.connect('gestaoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE login=?", (login,))
    dados = cursor.fetchall()
    conn.close()
    if len(dados) > 0:
        return True
    else:
        return False
    
def recuperarSenhaBD(login):
    conn = sqlite.connect('gestaoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT senha FROM usuarios WHERE login=?", (login,))
    dados = cursor.fetchone()
    conn.close()
    if dados:
        return dados[0]  # Retorna a senha encontrada
    else:
        return None  # Retorna None se o usuário não for encontrado
    
def alterarSenhaBD(login, nova_senha):
    conn = sqlite.connect('gestaoDB.sqlite')
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET senha=? WHERE login=?", (nova_senha, login))
    conn.commit()
    conn.close()