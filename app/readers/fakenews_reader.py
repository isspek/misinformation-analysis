import csv
import sqlite3
import glob

from app.utils import parse_url
from loguru import logger

'''
Fakenews datasets reader. Each dataset has in different format. Reader each dataset and index essential fields to sqlite db
'''
DB_NAME = 'fakenews_collection.db'
DB_PATH = '../../data/{}'.format(DB_NAME)
DB_TABLE = 'fakenews_collection'


def kaggle_fakenews():
    collection = 'kaggle_fakenews'
    i = 1
    rows = []
    with open('/Users/tmp/Documents/misinformation-analysis/data/kaggle-fakenews/data.csv', newline='') as csv_file:
        # skip header line
        next(csv_file)
        # bulk read entries from CSV (may break for too many items, switch to committing occasionally if)
        for row in csv.reader(csv_file, delimiter=',', quotechar='"'):
            #           id, headline, body, label, collection, source
            rows.append([i, row[1], row[2], row[3], collection, parse_url(row[0])])
            i += 1
        db_insert_fakenews(DB_PATH, DB_TABLE, rows)

def fakenewscorpus():
    collection = 'fakenewscorpus'
    i = 1
    rows = []
    # with open('/Users/tmp/Documents/misinformation-analysis/data/fakenewscorpus' )






def db_insert_fakenews(db_path, db_table, entries):
    # connect to sqlite db
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # purge table before inserting
    cur.execute('DELETE FROM {};'.format(db_table))
    # insert
    cur.executemany(
        'INSERT INTO {}(`id`, headline, `body`, `label`, `collection`, source) VALUES (?,?,?,?,?,?)'.format(db_table),
        entries)
    # commit to and close db
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # kaggle_fakenews()
    fakenewscorpus()
