
## PostgreSQL Connection Pooling

For some applications, the overhead PSQL imposes whenever a new connection opens can become a performance bottleneck.  There are tools, like [PgBouncer](https://pgbouncer.github.io/) that act as a PSQL proxy, and "pool" connections.   PgBouncer opens up a fixed number of connections to PSQL, and keeps those connections open. Database clients connect to PgBouncer, instead of PSQL directly, and PgBouncer proxies the client SQL commands on an existing PSQL connection.  

## Configuring PgBouncer

PgBouncer is already installed and configured on your **Saleor** instance.  To use it, you just need to change the Saleor database connection string in the **saleor/settings.py** file.

Open **saleor/settings.py**, find this line and change it from

```python
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://saleor:saleor@127.0.0.1:5432/saleor',
        conn_max_age=600)}
```

to (just changing connection string port number from **5432** to **6432**)

```python
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://saleor:saleor@127.0.0.1:6432/saleor',
        conn_max_age=600)}
```

and restart uwsgi:

```
sudo supervisorctl restart uwsgi
```
