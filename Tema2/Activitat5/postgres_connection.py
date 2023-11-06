import psycopg2

db_params = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "CalaClara21",
    "dbname": "world",
}

try:
    conn = psycopg2.connect(**db_params)
    print(conn)
except psycopg2.Error as e:
    print(f"Error: {e}")
