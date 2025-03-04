import sqlite3
import aiosqlite

class EmployeeData:
    def __init__(self, db_path="database/employee-data.db"):
        self.db_path = db_path
        self.conn = None

    async def connect(self):
        """Asynchronously connect to the employee database."""
        self.conn = await aiosqlite.connect(self.db_path)

    async def close(self):
        """Close the database connection."""
        if self.conn:
            await self.conn.close()

    async def get_database_info(self) -> str:
        """Retrieve schema information for the employee database."""
        async with self.conn.execute("SELECT name FROM sqlite_master WHERE type='table';") as cursor:
            tables = await cursor.fetchall()
        schema_info = "\n".join([table[0] for table in tables])
        return f"Employee Database Tables:\n{schema_info}"

    async def async_fetch_employee_data_using_sqlite_query(self, query: str):
        """Execute a SQL query and fetch employee data."""
        async with self.conn.execute(query) as cursor:
            rows = await cursor.fetchall()
        return rows

    async def verify_user_exists(self, username: str) -> str:
        """Check if the user exists in the employee database."""
        query = "SELECT 1 FROM employees WHERE name = ? LIMIT 1;"
        async with self.conn.execute(query, (username,)) as cursor:
            result = await cursor.fetchone()
        
        if result:
            return f"User {username} verified and exists in the system."
        else:
            return f"User {username} does not exist in the database. You will be added."

    async def insert_new_employee(self, name: str, age: int, department: str, position: str, salary: float, year_joined: int, region: str) -> None:
        """Insert a new employee into the employee database."""
        query = """
        INSERT INTO employees (name, age, department, position, salary, year_joined, region)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        async with self.conn.execute(query, (name, age, department, position, salary, year_joined, region)) as cursor:
            await self.conn.commit()
        print(f"Inserted new employee: {name}")