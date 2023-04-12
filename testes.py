import mysql.connector
import requests
import csv
import os
import time
from datetime import datetime, timedelta

mysql_host = 'localhost'
mysql_port = '3306'
mysql_user = 'orchard'
mysql_password = 'orchardpassword'
mysql_database = 'orchard'

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
    csv_data = response.content.decode('ISO-8859-1').splitlines()
    csv_reader = csv.reader(csv_data, delimiter=';', quotechar='"')
    header = next(csv_reader)

    # Deletes the current contents from table
    print("Deleting all rows from the table...")
    cursor2 = cnx.cursor()
    sql_delete = "DELETE FROM ORCHARD.CIAS_ABERTAS"
    cursor2.execute(sql_delete)
    cnx.commit()
    cursor2.close()
    print("All rows have been deleted.")

    print("Inserting the processed updated data in the local table...")
    for row in csv_reader:
        ### print(row)
        row = [None if x == '' else x for x in row]
        print("Fixed row values:")
        print(row)
        values = tuple(row)
        ### print(len(header), len(values))
        sql_insert = 'INSERT INTO ORCHARD.CIAS_ABERTAS ({}) VALUES ({})'.format(', '.join(header), ', '.join(['%s']*len(header)))
        cursor = cnx.cursor()
        cursor.execute(sql_insert, values)
        cnx.commit()
        cursor.close()
    print("Data has been inserted. Closing database connection.")
    # Close the connection
    cnx.close()

insert_csv_data()

# def schedule_insertion():
#     now = datetime.now()
#     print(f'Now: {now}')
#     target_time = datetime(now.year, now.month, now.day, 22, 40, 0)
#     print(f'Target time: {target_time}')
#     if now > target_time:
#         target_time += timedelta(days=1)

#     print(f'New target time: {target_time}')
#     time_to_wait = (target_time - now).total_seconds()
#     print(f'Time to wait: {time_to_wait}')
#     time.sleep(time_to_wait)
#     insert_csv_data()

# while True:
#     print('Entered the while true loop')
#     schedule_insertion()
