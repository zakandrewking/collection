# collection
Science for everyone

# Get started

PostgreSQL installation:

```shell
brew install postgresql
mkdir /Library/PostgreSQL
mkdir /Library/PostgreSQL/data
export PGDATA="/Library/PostgreSQL/data/"
sudo chown username $PGDATA
pg_ctl init
pg_ctl start
createdb collection
psql collection
```

Load the database:

```shell
python -m collection.load_database
```
