import pandas as pd 
import os
from sqlalchemy import create_engine
import logging

logging.basicConfig(
    filename = 'logs/ingestion_db.log',
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filemode = 'a'
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    ''' this function will load the CSVs as dataframe and ingest into db '''
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False) 

def load_raw_date():
    ''' this function will load the CSVs as dataframe and ingest into db '''
    for file in os.listdir('data'):
        if '.csv' in file: # chỉ xử lý những file có đuổi .csv
            df = pd.read_csv('data/'+file)
            logging.info('Ingesting {file} in db')
            ingest_db(df, file[:-4], engine) 
    end = time.time()
    total_time = (end - start)/60
    logging.info('----------Ingestion Complete----------')
    logging.info('Total Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()