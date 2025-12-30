import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="fastapi_db",
    user="postgres",
    password="1234",
    port="5433"
)
    
cur = conn.cursor()
cur.execute("SELECT id, name, email FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()