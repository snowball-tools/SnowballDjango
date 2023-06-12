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

### Railway Setup

```bash
railway login
railway link
```

### Run

```bash
railway shell
railway run python manage.py migrate && python manage.py collectstatic --noinput && gunicorn snowballwebapp.wsgi
```

## Deploy

```bash
railway up
```

## Built With

* [Django](https://www.djangoproject.com/)
* [Railway](https://railway.app/)
* [PostgreSQL](https://www.postgresql.org/)
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) using [django-bootstrap-v5](https://django-bootstrap-v5.readthedocs.io/en/latest/quickstart.html)
