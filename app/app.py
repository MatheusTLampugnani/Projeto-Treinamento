from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="formulario"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nome_condutor = request.form['nome_condutor']
        nome_empresa = request.form['nome_empresa']
        veiculo_usado = request.form['veiculo_usado']
        data_treinamento = request.form['data_treinamento']
        treinamento = request.form['treinamento']
        caminhao = request.form['caminhao']
        conhecimento = request.form['conhecimento']
        organizacao = request.form['organizacao']
        instalacoes = request.form['instalacoes']
        conteudo = request.form['conteudo']
        qualidade = request.form['qualidade']
        avaliacao = request.form['avaliacao']
        instrutor = request.form['instrutor']
        comentario = request.form['comentario']

        # Insere os dados no banco de dados
        sql = "INSERT INTO usuarios (nome_condutor, nome_empresa, veiculo_usado, data_treinamento, treinamento, caminhao, conhecimento, organizacao, instalacoes, conteudo, qualidade, avaliacao, instrutor, comentario) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)"
        val = (nome_condutor, nome_empresa, veiculo_usado, data_treinamento,treinamento, caminhao, conhecimento, organizacao, instalacoes, conteudo, qualidade, avaliacao, instrutor, comentario)
        cursor.execute(sql, val)
        db.commit()

        return 'Dados inseridos com sucesso no banco de dados!'

if __name__ == '__main__':
    app.run(debug=True)