from main import config
import mysql.connector


def conectar():
    # Cria uma conexão
    conexao = mysql.connector.connect(**config)
    return conexao

def criar_tabela():

    # Função para criar uma tabela (exemplo)
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Exemplo de criação de tabela
        tabela_sql = '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_condutor VARCHAR(255),
            nome_empresa VARCHAR(255),
            veiculo_usado VARCHAR(255),
            data_treinamento VARCHAR(55)
        )
        '''
        cursor.execute(tabela_sql)
        print("Tabela criada com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")


criar_tabela()