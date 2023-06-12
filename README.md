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

### Running

```bash
railway shell
railway run python manage.py migrate && python manage.py collectstatic --noinput && gunicorn snowballwebapp.wsgi
```

## Deployment

```bash
railway up
```

## Built With

* [Django](https://www.djangoproject.com/)
* [Railway](https://railway.app/)