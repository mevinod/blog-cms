# blog-cms
This is a very simple personal blog management system, built with python-flask and postgres as backend.

## Instructions to run standalone
### precondition
> Before starting, you should have connection parameters to postgres and it should be reachable

- Either update the database parameters in the config.py OR export those as environment variable
 `export DATABASE_URL='postgresql://postgres:mysecretpassword@localhost/postgres'`
- Now, run `python3 app.py`

## Instructions to run docker
### precondition
> Before starting, you should have connection parameters to postgres and it should be reachable
- export database parameters as environment variable
 `export DATABASE_URL='postgresql://postgres:mysecretpassword@localhost/postgres'`
- Now, run `docker run -e DATABASE_URL='postgresql://postgres:mysecretpassword@localhost/postgres' --network="host" <image-name>`
