import sqlite3

# Define database path
db_path = "../employee-data.db"

# Connect to SQLite (creates the file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Read SQL commands from your script
sql_script_path = "populate_employees.sql"
with open(sql_script_path, "r") as file:
    sql_script = file.read()

# Execute SQL script
cursor.executescript(sql_script)

# Commit and close
conn.commit()
conn.close()

print(f"✅ Database '{db_path}' has been created and populated.")