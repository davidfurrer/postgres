# Postgres example database

## Docker

To create postgres database:

```
docker run -p 5432:5432 --name postgres-test postgres
```

To create postgres database with credentials:

```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

To create admin panel:

```
docker run -p 5555:80 --name admin-postgres -e PGADMIN_DEFAULT_EMAIL='david' -e PGADMIN_DEFAULT_PASSWORD='passoword' dpage/pgadmin4
```

This provides a UI which you can see at localhost:5555 (in this case).

You can connect to database in admin panel
with username, password: postgres, postgres (if default docker).

## Setting up credentials

Create `database.ini` and fill in the following with your credentials:

```
[postgresql]
host=localhost
database=postgres
user=postgres
password=postgres

```

Put `database.ini` in `.gitignore`.

Ref: https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43
