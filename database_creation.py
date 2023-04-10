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
    "  DENOM_SOCIAL VARCHAR(200) NULL,"
    "  DENOM_COMERC VARCHAR(200) NULL,"
    "  DT_REG DATE NULL,"
    "  DT_CONST DATE NULL,"
    "  DT_CANCEL DATE NULL,"
    "  MOTIVO_CANCEL VARCHAR(200) NULL,"
    "  SIT VARCHAR(10) NULL,"
    "  DT_INI_SIT DATE NULL,"
    "  CD_CVM INT NULL,"
    "  SETOR_ATIV VARCHAR(100) NULL,"
    "  TP_MERC VARCHAR(10) NULL,"
    "  CATEG_REG VARCHAR(50) NULL,"
    "  DT_INI_CATEG DATE NULL,"
    "  SIT_EMISSOR VARCHAR(10) NULL,"
    "  DT_INI_SIT_EMISSOR DATE NULL,"
    "  CONTROLE_ACIONARIO VARCHAR(100) NULL,"
    "  TP_ENDER VARCHAR(20) NULL,"
    "  LOGRADOURO VARCHAR(100) NULL,"
    "  COMPL VARCHAR(100) NULL,"
    "  BAIRRO VARCHAR(50) NULL,"
    "  MUN VARCHAR(50) NULL,"
    "  UF VARCHAR(2) NULL,"
    "  PAIS VARCHAR(50) NULL,"
    "  CEP VARCHAR(8) NULL,"
    "  DDD_TEL VARCHAR(2) NULL,"
    "  TEL VARCHAR(9) NULL,"
    "  DDD_FAX VARCHAR(2) NULL,"
    "  FAX VARCHAR(9) NULL,"
    "  EMAIL VARCHAR(100) NULL,"
    "  TP_RESP VARCHAR(10) NULL,"
    "  RESP VARCHAR(200) NULL,"
    "  DT_INI_RESP DATE NULL,"
    "  LOGRADOURO_RESP VARCHAR(100) NULL,"
    "  COMPL_RESP VARCHAR(100) NULL,"
    "  BAIRRO_RESP VARCHAR(50) NULL,"
    "  MUN_RESP VARCHAR(50) NULL,"
    "  UF_RESP VARCHAR(2) NULL,"
    "  PAIS_RESP VARCHAR(50) NULL,"
    "  CEP_RESP VARCHAR(8) NULL,"
    "  DDD_TEL_RESP VARCHAR(2) NULL,"
    "  TEL_RESP VARCHAR(9) NULL,"
    "  DDD_FAX_RESP VARCHAR(2) NULL,"
    "  FAX_RESP VARCHAR(9) NULL,"
    "  EMAIL_RESP VARCHAR(100) NULL,"
    "  CNPJ_AUDITOR VARCHAR(18) NULL,"
    "  AUDITOR VARCHAR(100) NULL"
    ")")

cursor.execute(create_table_query)
print("Tabela criada!")

# Finaliza a conexão com a base de dados
cnx.commit()
cursor.close()
cnx.close()