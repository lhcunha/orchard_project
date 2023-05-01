import mysql.connector
import requests
import csv
import os
import time
from datetime import datetime, timedelta

mysql_host = os.environ['MYSQL_HOST']
mysql_port = os.environ['MYSQL_PORT']
mysql_user = os.environ['MYSQL_USER']
mysql_password = os.environ['MYSQL_PASSWORD']
mysql_database = os.environ['MYSQL_DATABASE']

def insert_csv_data():
    while True:
        try:
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

            # Parse the CSV data
            print("Processing the collected data...")
            csv_data = response.content.decode('ISO-8859-1').splitlines()
            csv_reader = csv.reader(csv_data, delimiter=';', quotechar='"')
            header = next(csv_reader)

            # Get the existing data from the table
            cursor1 = cnx.cursor()
            cursor1.execute("SELECT * FROM orchard.CIAS_ABERTAS")
            existing_data = cursor1.fetchall()
            cursor1.close()

            # Build a dictionary of the existing data keyed by CNPJ_CIA
            existing_data_dict = {}
            for row in existing_data:
                existing_data_dict[row[1]] = row
            ### print(existing_data_dict)

            # Identify new and updated records and insert/update them as necessary
            cursor2 = cnx.cursor()
            for row in csv_reader:
                row = [None if x == '' else x for x in row]
                cnpj_cia = row[0]
                ### print(f'CNPJ da empresa do csv coletado da API: {cnpj_cia}')
                if cnpj_cia in existing_data_dict:
                    # Update the existing record
                    existing_row = existing_data_dict[cnpj_cia]
                    ### print (f'existing_row: {existing_row[2]}')
                    values = tuple(row + list(existing_row[len(row): -1]))
                    sql_update = 'UPDATE orchard.CIAS_ABERTAS SET {} WHERE id = {}'.format(
                        ', '.join([h + ' = %s' for h in header]),
                        existing_row[0]
                    )
                    cursor2.execute(sql_update, values)
                else:
                    # Insert a new record
                    values = tuple(row)
                    sql_insert = 'INSERT INTO orchard.CIAS_ABERTAS ({}) VALUES ({})'.format(
                        ', '.join(header),
                        ', '.join(['%s'] * len(header))
                    )
                    cursor2.execute(sql_insert, values)

            cnx.commit()
            cursor2.close()
            print("Data has been inserted/updated. Closing database connection.")
            # Close the connection
            cnx.close()
            break

        except mysql.connector.errors.ProgrammingError as e:
            print("MySQL error occurred:", e)
            cnx.close()
            time.sleep(60)  # Wait 60 seconds before trying again
            continue

insert_csv_data()
