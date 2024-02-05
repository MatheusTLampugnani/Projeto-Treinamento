from flask import Flask, render_template, request, redirect, url_for
from main import config, conectar
import mysql.connector

app = Flask(__name__)

def desconectar(conexao):
    # Função para fechar a conexão com o banco de dados
    if conexao.is_connected():
        conexao.close()

@app.route('/')
def index():
    # Função para exibir todos os usuários
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    desconectar(conexao)

    return render_template('./index.html', usuarios=usuarios)
@app.route('/', methods=['POST'])
def adicionar_usuario():
    # Função para adicionar um novo usuário
    if request.method == 'POST':
        nome_condutor = request.form['nome_condutor']
        nome_empresa = request.form['nome_empresa']
        veiculo_usado = request.form['veiculo_usado']
        data_treinamento = request.form['data_treinamento']

        conexao = conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute('INSERT INTO usuarios (nome_condutor,nome_empresa, veiculo_usado,data_treinamento) VALUES (%s, %s, %s, %s)'(nome_condutor, nome_empresa, veiculo_usado, data_treinamento))
            conexao.commit()
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar usuário: {err}")
            conexao.rollback()
        finally:
            desconectar(conexao)

    return redirect(url_for('index'))

def inserir_usuario(nome_condutor,
            nome_empresa,
            veiculo_usado,
            data_treinamento):
    # Função para inserir um novo usuário
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Exemplo de inserção de dados
        insercao_sql = "INSERT INTO usuarios (nome_condutor,nome_empresa, veiculo_usado,data_treinamento) VALUES (%s, %s, %s, %s)"
        dados_usuario = (nome_condutor,
            nome_empresa,
            veiculo_usado,
            data_treinamento)
        cursor.execute(insercao_sql, dados_usuario)
        conexao.commit()
        print("Usuário inserido com sucesso!")

    except mysql.connector.Error as err:
        conexao.rollback()
        print(f"Erro: {err}")


inserir_usuario('Matheus',
            'volus',
            'Supra mk3',
            '28/12/2023')
