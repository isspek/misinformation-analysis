from sqlalchemy import create_engine
from pathlib import Path
import logging
import pandas as pd

data_dir = Path('data')
log = logging.getLogger('logger')

DB_NAME = 'articles.db'
TABLE = 'articles'
DATE = 'date'
SOURCE = 'source'
TITLE = 'name'
CLEANED_TEXT = 'content'

disk_engine = create_engine('sqlite:///./data/{}'.format(DB_NAME), convert_unicode=True)

log.info("Connected to {}".format(DB_NAME))

# select name and content from the table and save for processing & analysis
content_df = pd.read_sql_query("SELECT {}, {}, {}, {} FROM {}".format(TITLE,SOURCE,CLEANED_TEXT,DATE, TABLE), disk_engine)
content_df_out = 'nela_2018_df.pkl'
content_df.to_pickle(data_dir/content_df_out)

log.info("Data transfer is done.")
