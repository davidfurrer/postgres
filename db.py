import psycopg2

# ref: https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43

# pipenv install psycopg2-binary
# docker run -p 5432:5432 --name postgres-test postgres
# docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres

# admin
# docker run -p 5555:80 --name admin-postgres -e PGADMIN_DEFAULT_EMAIL='david' -e PGADMIN_DEFAULT_PASSWORD='passoword' dpage/pgadmin4

# in admin panel
# adress: use IP , username, password: postgres, postgres


from config import config

# Establish a connection to the database by creating a cursor object

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
