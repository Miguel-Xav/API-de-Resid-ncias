import sqlite3

# Função para fazer uma conexão com o SQLite
def get_db_connection():
    conn = sqlite3.connect('database_res.db')
    return conn

# Função para criar uma tabela se ela já não estiver criada
def criar_tabela():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS database_res(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT,
        cep INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar uma residência
def adicionar_res(nome, endereco, cep):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO database_res (nome, endereco, cep) VALUES (?, ?, ?)', (nome, endereco, cep))
    conn.commit()
    id_residencia = cursor.lastrowid
    conn.close()
    return id_residencia

# Função para listar as residências
def listar_res():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM database_res')
    database_res = cursor.fetchall()
    conn.close()
    return database_res

# Função para editar uma residência
def edit_res(id, novo_nome, novo_endereco, novo_cep):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE database_res SET nome = ?, endereco = ?, cep = ? WHERE id = ?', (novo_nome, novo_endereco, novo_cep, id))
    conn.commit()
    conn.close()

# Função para deletar uma residência
def deletar_res(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM database_res WHERE id = ?', (id,))
    conn.commit()
    conn.close()
