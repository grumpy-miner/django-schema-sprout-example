# django-schema-sprout-example

In this example we're connecting with AACT (Aggregated Analysis of ClinicalTrials.gov) database.
To be able to connect to database you need to sign up to the site https://aact.ctti-clinicaltrials.org

Since database uses Postgres v11 we will be using Django 4.1.


## Setting up

Clone the repository
```sh
git clone git@github.com:grumpy-miner/django-schema-sprout-example.git
```

Inside repo directory create virtual enviroment and install requirements.

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.dev` to `.env` and set up file.
(To set up account sign up at https://aact.ctti-clinicaltrials.org)

```sh
cp .env.dev .env
vim .env
```

Go into `sprout_schema_example` directory and let's collect static files.

```sh
cd sprout_schema_example
./manage.py collectstatic
```

Run server

```sh
./manage.py runserver
```

It will take some time to start the server as AACT has a lot of tables and schemas.

