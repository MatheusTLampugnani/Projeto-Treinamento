import mysql.connector

# Configurações de conexão
config = {
  'user': 'MatheusLampugnani',
  'password': 'L@mpugn4n1',
  'host': 'localhost',  # ou o endereço IP do servidor MySQL
  'database': 'teste',
  'raise_on_warnings': True
}

# Cria uma conexão
def conectar():
    # Cria uma conexão
  try:
      conexao = mysql.connector.connect(**config)
      print('conectado')
      return conexao

      # Se a conexão for bem-sucedida, você pode começar a executar consultas aqui
  except mysql.connector.Error as err:
      print(f"Erro: {err}")



