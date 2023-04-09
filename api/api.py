import mysql.connector
import requests
import csv
import os
from datetime import datetime, time, timedelta

mysql_host = os.environ['MYSQL_HOST']
mysql_port = os.environ['MYSQL_PORT']
mysql_user = os.environ['MYSQL_USER']
mysql_password = os.environ['MYSQL_PASSWORD']
mysql_database = os.environ['MYSQL_DATABASE']

def insert_csv_data():
    # Connect to the MySQL container
    cnx = mysql.connector.connect(
    host=mysql_host,
    port=mysql_port,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
    )
    # Get the CSV data from the URL
    print("Gathering data from the external API...")
    csv_url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv'
    response = requests.get(csv_url)
    print("Data has been gathered.")

    # Parse the CSV data and insert it into the CIAS_ABERTAS table
    print("Processing the collected data...")
    csv_data = response.content.decode('utf-8').splitlines()
    csv_reader = csv.reader(csv_data, delimiter=',', quotechar='"')
    header = next(csv_reader)
    print("Inserting the processed data in the local table...")
    for row in csv_reader:
        sql = 'INSERT INTO orchard.CIAS_ABERTAS ({}) VALUES ({})'.format(', '.join(header), ', '.join(['%s']*len(header)))
        values = tuple(row)
        cursor = cnx.cursor()
        cursor.execute(sql, values)
        cnx.commit()
        cursor.close()
    print("Data has been inserted. Closing database connection.")
    # Close the connection
    cnx.close()

insert_csv_data()

# def schedule_insertion():
#     now = datetime.now()
#     target_time = datetime(now.year, now.month, now.day, 9, 0, 0)
#     if now > target_time:
#         target_time += timedelta(days=1)

#     time_to_wait = (target_time - now).total_seconds()
#     time.sleep(time_to_wait)
#     insert_csv_data()

# while True:
#     schedule_insertion()
