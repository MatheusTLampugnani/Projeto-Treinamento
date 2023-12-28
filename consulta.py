

cursor = conexao.cursor()

# Exemplo de consulta SQL
consulta_sql = "SELECT * FROM usuarios"
cursor.execute(consulta_sql)

# Obtém os resultados
resultados = cursor.fetchall()

# Itera sobre os resultados
for linha in resultados:
    print(linha)

# Certifique-se de fechar o cursor após o uso
cursor.close()
