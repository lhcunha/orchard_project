import mysql.connector
import time

# Configurações de conexão com a base de dados
host = 'mysql'
user = 'orchard'
password = 'orchardpassword'
database = 'orchard'
port = '3306'


try:
    #tenta estabelecer a conexão
    cnx = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
    print("Conexão com o MySQL foi realizada com sucesso!")
    cnx.close()
except mysql.connector.Error as err:
    # se houver um erro, espera 1 segundo e tenta novamente
    print(f"Erro ao conectar com o MySQL: {err}")
    time.sleep(1)
