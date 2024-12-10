import os
import pyodbc
import pandas as pd

# Get connection details from environment variables (do not hardcode sensitive information)
db_config = {
    "server": os.getenv("DB_SERVER", "localhost\\SQLEXPRESS"),  # Default to localhost\SQLEXPRESS
    "database": os.getenv("DB_DATABASE", "YourDatabaseName"),
    "username": os.getenv("DB_USERNAME", "admin"),
    "password": os.getenv("DB_PASSWORD", "your_password_here"),
    "driver": os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
}

# SQL query to execute
query = """
SELECT 
    a.id, 
    a.Nombre,
    a.NumSerie,
    a.Siglas, 
    b.*, 
    c.Canal, 
    d.Numero, 
    d.Nombre
FROM Remotas AS a
JOIN SensoresRemotas AS c
    ON a.id = c.idRemotas
RIGHT JOIN DatosUTR AS b
    ON c.id = b.idSensoresRemotas
LEFT JOIN Sensores AS d
    ON c.idSensores = d.id
ORDER BY a.id ASC;
"""

# Prompt the user to select the connection type (local or remote)
connection_type = input("Choose connection type ('local' or 'remote'): ").strip().lower()

if connection_type == "local":
    print("Connecting to the database locally...")
    db_config["server"] = "localhost\\SQLEXPRESS"  # Local SQL Server instance
elif connection_type == "remote":
    print("Connecting to the remote database...")
    db_config["server"] = "10.2.251.149"  # Remote server IP (adjust accordingly)
else:
    print("Invalid input. Defaulting to local connection.")
    db_config["server"] = "localhost\\SQLEXPRESS"

# Define the output file path
output_file = "output.csv"

try:
    # Build the connection string
    connection_string = (
        f"DRIVER={db_config['driver']};"
        f"SERVER={db_config['server']};"
        f"DATABASE={db_config['database']};"
        f"UID={db_config['username']};"
        f"PWD={db_config['password']};"
    )
    
    # Connect to SQL Server
    conn = pyodbc.connect(connection_string)
    print("Successfully connected to the database.")
    
    # Execute the query and load the results into a DataFrame
    df = pd.read_sql(query, conn)
    
    # Export the results to a CSV file
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Data successfully exported to {output_file}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection if it was opened
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")
