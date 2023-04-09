import mysql.connector
import time

# Configurações de conexão com a base de dados
host = 'localhost'
user = 'orchard'
password = 'orchardpassword'
database = 'orchard'
port = '3306'


try:
    # tenta estabelecer a conexão
    cnx = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database, auth_plugin='mysql_native_password')
    print("Conexão com o MySQL foi realizada com sucesso!")
except mysql.connector.Error as err:
    # se houver um erro, espera 1 segundo e tenta novamente
    print(f"Erro ao conectar com o MySQL: {err}")
    time.sleep(1)



# Cria o cursor
cursor = cnx.cursor()

# Cria a tabela
print("Criando tabela...")

table_name = 'CIAS_ABERTAS'
create_table_query = (
    "CREATE TABLE IF NOT EXISTS " + table_name + " ("
    "  id INT AUTO_INCREMENT PRIMARY KEY,"
    "  CNPJ_CIA VARCHAR(18) NOT NULL,"
    "  DENOM_SOCIAL VARCHAR(200) NOT NULL,"
    "  DENOM_COMERC VARCHAR(200) NOT NULL,"
    "  DT_REG DATE NOT NULL,"
    "  DT_CONST DATE NOT NULL,"
    "  DT_CANCEL DATE,"
    "  MOTIVO_CANCEL VARCHAR(200),"
    "  SIT VARCHAR(10) NOT NULL,"
    "  DT_INI_SIT DATE NOT NULL,"
    "  CD_CVM INT NOT NULL,"
    "  SETOR_ATIV VARCHAR(100),"
    "  TP_MERC VARCHAR(10) NOT NULL,"
    "  CATEG_REG VARCHAR(50) NOT NULL,"
    "  DT_INI_CATEG DATE NOT NULL,"
    "  SIT_EMISSOR VARCHAR(10) NOT NULL,"
    "  DT_INI_SIT_EMISSOR DATE NOT NULL,"
    "  CONTROLE_ACIONARIO VARCHAR(100),"
    "  TP_ENDER VARCHAR(20) NOT NULL,"
    "  LOGRADOURO VARCHAR(100),"
    "  COMPL VARCHAR(100),"
    "  BAIRRO VARCHAR(50),"
    "  MUN VARCHAR(50),"
    "  UF VARCHAR(2),"
    "  PAIS VARCHAR(50),"
    "  CEP VARCHAR(8),"
    "  DDD_TEL VARCHAR(2),"
    "  TEL VARCHAR(9),"
    "  DDD_FAX VARCHAR(2),"
    "  FAX VARCHAR(9),"
    "  EMAIL VARCHAR(100),"
    "  TP_RESP VARCHAR(10),"
    "  RESP VARCHAR(200),"
    "  DT_INI_RESP DATE NOT NULL,"
    "  LOGRADOURO_RESP VARCHAR(100),"
    "  COMPL_RESP VARCHAR(100),"
    "  BAIRRO_RESP VARCHAR(50),"
    "  MUN_RESP VARCHAR(50),"
    "  UF_RESP VARCHAR(2),"
    "  PAIS_RESP VARCHAR(50),"
    "  CEP_RESP VARCHAR(8),"
    "  DDD_TEL_RESP VARCHAR(2),"
    "  TEL_RESP VARCHAR(9),"
    "  DDD_FAX_RESP VARCHAR(2),"
    "  FAX_RESP VARCHAR(9),"
    "  EMAIL_RESP VARCHAR(100),"
    "  CNPJ_AUDITOR VARCHAR(18),"
    "  AUDITOR VARCHAR(100)"
    ")")

cursor.execute(create_table_query)
print("Tabela criada!")

# Finaliza a conexão com a base de dados
cnx.commit()
cursor.close()
cnx.close()