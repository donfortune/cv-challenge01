import psycopg2

# Database connection details
DATABASE = {
    "host": "mydb.cbi48swys3b5.us-east-1.rds.amazonaws.com",
    "port": "5432",
    "dbname": "donfortune1",
    "user": "postgres",
    "password": "Tangban1.",  # Replace with your actual password
}

try:
    # Connect to the database
    connection = psycopg2.connect(**DATABASE)
    print("Successfully connected to the database!")
    
    # Perform queries
    with connection.cursor() as cursor:
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        print("Current Timestamp:", result)
    
    # Close the connection
    connection.close()
except Exception as e:
    print(f"Failed to connect to the database: {e}")
