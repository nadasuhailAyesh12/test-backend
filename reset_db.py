import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = "elb"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
    print(f"✅ Dropped database '{DB_NAME}'")

    cursor.execute(f"CREATE DATABASE {DB_NAME};")
    print(f"✅ Created database '{DB_NAME}'")

    cursor.close()
    conn.close()

except Exception as e:
    print(f"❌ Error: {e}")
