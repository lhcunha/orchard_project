import mysql.connector

# Configurações de conexão com a base de dados
host = 'localhost'
user = 'orchard'
password = 'orchardpassword'
database = 'orchard'
port = 3306

try:
    # Cria a conexão com a base de dados
    cnx = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
    print("Conexão com o MySQL foi realizada com sucesso!")
    cnx.close()
except mysql.connector.Error as err:
    print(f"Erro ao conectar com o MySQL: {err}")

