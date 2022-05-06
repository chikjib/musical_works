# MUSICAL WORKS PROJECT
A musical work consists of the musical notes and lyrics (if any) in a musical composition. A musical work may be fixed in any form, such as a piece of sheet music or a sound recording. It is usually represented by metadata like: title, contributors, roles, duration.
This application helps to upload works_metadata into a database, and it includes an api view built using Django Restful Framework that enables anyone to access data related to a particular musical work using the ISWC (International Standard Musical Work Code) identification number.

# How to Install and Run the Project
1. Create a virtual environment using and install the requirements by running pip install pip install -r requirements.txt on your terminal.

2. Create a postgres Database and change the database details in the settings; { look for a folder music_config in the downloaded file }, and change the default settings below;

### Database
#### https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'music_works_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'POST': '',
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}
3. Enter the virtual environment and cd:/~django_projects/music_config then run python manage.py migrate

# Usage
1. To upload the works_metadata.csv, from the command line, run python manage.py load_data
You should get the message: "Data loaded Successfully"

2. To access the api view; run python manage.py runserver 
3. Go to your browser and type in http://localhost:8000/api/
4. To access a single record by ISWC number use: http://localhost:8000/api/{ISWC}

## PART 1 QUESTIONS
1. Describe briefly the matching and reconciling method chosen.

#### ANSWER 1
I used pandas to analyse the data, by taking a union of repeated contributors by title and then removing duplicates, using drop_duplicates(), before adding the reconciled records to the database.


2. We constantly receive metadata from our providers, how would
you automatize the process?

#### ANSWER 2
I will have to write a scripts, that will append the data to the previous csv works_metadata.csv file which will in turn append the rest of the data to the database, or better still remove the records there and replace with an updated works_metadata.csv records.

## PART 2 QUESTIONS
1. Imagine that the Single View has 20 million musical works, do
you think your solution would have a similar response time?

### ANSWER 1:
Yes, because the response is in json and its just a single query lookup in the lookup viewset and am not using a Filter which would have been filtering every single data which is costly.

2. If not, what would you do to improve it?
