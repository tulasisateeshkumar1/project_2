
import mysql.connector
from mysql.connector import Error

try:
    # 1. Establish the connection
    conn = mysql.connector.connect(
        host="localhost",
        user="sateesh",
        password="2181",
        database="sateesh"
    )

    if conn.is_connected():
        # Use dictionary=True to return rows as dictionaries instead of tuples
        cursor = conn.cursor(dictionary=True)

        # 2. Insert data (always use %s placeholders to prevent SQL injection)
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(insert_query, ("Alice", "alice@example.com"))
        conn.commit()  # Commit is required for write operations

        # 3. Query data
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except Error as e:
    print(f"Database error: {e}")

finally:
    # 4. Clean up resources
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
