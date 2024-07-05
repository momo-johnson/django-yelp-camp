# Django Yelp Camp
[![Python Version](https://img.shields.io/badge/python-3.12.3-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django==5.0.6-brightgreen.svg)](https://djangoproject.com)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/momojohnson/django-yelp-camp
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Setup the local configurations:

```
 create .env and setup your configurations
 SECRET_KEY=XXXX
 ALLOWED_HOSTS=.localhost, .herokuapp.com, 127.0.0.1
 DATABASE_URL=XXXX
 DEBUG=XXXX
 CLOUDINARY_CLOUD_NAME=XXXX
 CLOUDINARY_API_KEY=XXXX
 COUDINARY_API_SECRET=XXXX
 GOOGLE_API_KEY=XXXX
 EMAIL_BACKEND=XXXX
 EMAIL_HOST=XXXX
 EMAIL_PORT=XXXX
 EMAIL_HOST_USER=XXXX
 EMAIL_HOST_PASSWORD=XXXX
 EMAIL_USE_TLS=XXXX
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.