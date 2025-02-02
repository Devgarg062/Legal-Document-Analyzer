import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"  # Replace with your actual MySQL root password
)

# Create a cursor object
cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS legal_doc_analyzer")

# Close the connection
cursor.close()
conn.close()

print("Database created successfully.")
