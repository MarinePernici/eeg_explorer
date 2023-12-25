import psycopg2

conn = psycopg2.connect(
    dbname="spectre",
    user="marine_pernici",
    password="123456",
    host="127.0.0.1"
)

cur = conn.cursor()
# cur.execute("""
#     CREATE TABLE ma_table (
#         id SERIAL PRIMARY KEY,
#         colonne1 VARCHAR(100),
#         colonne2 INT
#     )
# """)
conn.commit()
cur.close()

conn.close()
