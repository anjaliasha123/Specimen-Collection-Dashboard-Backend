import psycopg2
import time
import os
import dotenv



DB_HOST = os.environ.get('POSTGRES_HOST', 'pg_db')
DB_PORT = os.environ.get('POSTGRES_PORT', '5432')
DB_USER = os.environ.get('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'mypwd')

def check_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD
            )
            conn.close()
            print("PostgreSQL is ready!")
            break
        except Exception as e:
            print(f"Waiting for PostgreSQL... {e}")
            time.sleep(2)

if __name__ == "__main__":
    check_postgres()
