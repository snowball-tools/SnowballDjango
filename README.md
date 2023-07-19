# Snowball Web App

Django web app with postgresql database

## Getting Started

### Virtual Environment

| Command | Task |
| --- | --- |
| `python -m venv venv` | create |
| `. venv/bin/activate` | activate |
| `deactivate` | deactivate |

### Dependencies

```bash
pip install -r requirements.txt
```

### Local DB

`brew install postgresql`

| Command | Task |
| --- | --- |
| `createdb <DB_NAME>` | init db |
| `psql <DB_NAME>` | enter shell |


### DB Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run locally

```bash
python manage.py runserver
```

### Create Superuser

```bash
python manage.py createsuperuser
```

## Built With

* [Django](https://www.djangoproject.com/)
* [Postgres](https://www.postgresql.org/)