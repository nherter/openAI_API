import sqlite3

conn = sqlite3.connect("token_usage.db")
c = conn.cursor()

c.execute("""
SELECT * FROM response
""")

rows = c.fetchall()

for row in rows:
    print(row)

conn.close()