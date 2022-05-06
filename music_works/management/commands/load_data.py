from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from music_works.models import Work_Metadata
import pandas as pd
import numpy as np

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the music works meta data from the CSV file,
first truncate the table in the Postgres database or destroy the database.

Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from works_metadata.csv"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Work_Metadata.objects.exists():
            print('Works Metadata already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Loading Works metadata")

        # Code to load the data into database
        
        # Read csv file using Pandas
        dbframe = pd.read_csv(csv_file,encoding='utf-8')
        
        dbframe['contributors'] = dbframe.groupby(['title'])['contributors'].transform(lambda x :  '|'.join(x))
        
        dpn = dbframe.dropna()
        dp = dpn.drop_duplicates(subset="contributors")
        # print(dp)
        
        df = dp['contributors'].str.split("|")
        dpdf = df.drop_duplicates()
        
        # print(dpdf['contributors'])
        joined_contr= dpdf.str.join("|")
        dtitle = dp['title']
        diswc = dp['iswc']
        dfinal = pd.concat([dtitle,joined_contr,diswc],axis=1)
        # print(dfinal)
        
        for dbframef in dfinal.itertuples():
            
            # Insert into the database
            obj = Work_Metadata.objects.create(title=dbframef.title,contributors=dbframef.contributors,iswc=dbframef.iswc)
            print(type(obj))
            obj.save()
        
        print("Data loaded successfully.")
       
