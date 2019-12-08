import psycopg2
from config import config

# Obtain the configuration parameters
params = config()
# Connect to the PostgreSQL database
con = psycopg2.connect(**params)

cur = con.cursor()

cur.execute("select id, name from employees")

rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()
con.close()
