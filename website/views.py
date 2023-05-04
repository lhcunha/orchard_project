from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)
mysql_host = os.getenv("MYSQL_HOST", "mysql")
mysql_port = os.getenv("MYSQL_PORT", 3306)
mysql_user = os.getenv("MYSQL_USER", "orchard")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_database = os.getenv("MYSQL_DATABASE", "orchard")

# Configure database connection
db = mysql.connector.connect(
  host = mysql_host,
  user = mysql_user,
  password = mysql_password,
  database = mysql_database
)

# Define route to display companies grouped by industrial segment
@app.route('/')
def companies_by_segment():
    # Query database to get companies grouped by segment
    cursor = db.cursor()
    query = "SELECT SETOR_ATIV, GROUP_CONCAT(DENOM_COMERC SEPARATOR ', ') as companies FROM CIAS_ABERTAS \
            WHERE SIT = 'ATIVO' AND TP_MERC = 'BOLSA' GROUP BY SETOR_ATIV"
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Render HTML template with results
    return render_template('companies.html', results=results)

if __name__ == '__main__':
  app.run(debug=True)
