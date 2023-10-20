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

```sh
pip install -r requirements.txt
```

### Development

```sh
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn snowballwebapp.wsgi
```


## Built With

* [Django](https://www.djangoproject.com/)
* [Postgre](https://www.postgresql.org/)
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) using [django-bootstrap-v5](https://django-bootstrap-v5.readthedocs.io/en/latest/quickstart.html)
* [drf-social-oauth2](https://github.com/wagnerdelima/drf-social-oauth2)
* [django-rest-framework](https://www.django-rest-framework.org/)