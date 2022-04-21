# my-hood

This is a neighborhood platform that helps users connect and keep tab of the happenings within their neighborhoods. It is aimed at creating a connected community with residents more connected with their local businesses. 
## Features

- Django 4.0+
- Uses Pipenv the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.

## Screenshots

 <img src="https://github.com/amani-joseph/my-hood/blob/master/screenshots/0.png?raw=true" > 

 <img src="https://github.com/amani-joseph/my-hood/blob/master/screenshots/1.png?raw=true" > 

<img src="https://github.com/amani-joseph/my-hood/blob/master/screenshots/2.png?raw=true" > 

<img src="https://github.com/amani-joseph/my-hood/blob/master/screenshots/3.png?raw=true" > 

<img src="https://github.com/amani-joseph/my-hood/blob/master/screenshots/4.png?raw=true" > 

 <img src="https://github.com/amani-joseph/my-hood/blob/master/screenshots/5.png?raw=true" > 

 
### Dependencies

In order for you to use the content on this repo ensure you have the following:

- A computer that runs on either of the following; (Windows 7+, Linux, Mac OS)
- Python 3.6+

## How to install

```bash
#clone the repo
git clone https://github.com/amani-joseph/my-hood.git
# install virtual environment
$ python3 -m venv venv
#actictvate virtual environment
$ . venv/bin/active
#Install all dependecies
$ pip install -r requirements.txt
# Make databases and make migrations
$ python manage.py makemigrations
$ python manage.py migrate
#create a super user
$ python manage.py createsuperuser
#4. Running the application
$ python3 manage.py runserver



```

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'
```

These settings(and their default values) are only used on staging and production environments.

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
```

## Deployment

It is possible to deploy to Heroku or to your own server.

### Heroku

```bash
$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`
```

## License

The MIT License (MIT)

Copyright (c) 2022 Amani Joseph

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
