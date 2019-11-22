import pandas as pd
from pathlib import Path
import os
import dropbox
import configparser

config = configparser.ConfigParser()
config_path = Path('../config.ini')
config.read(config_path)

def read_from_json(file_path:str, save = False) -> pd.DataFrame:
    """
    Reads dataset in json form, and then return data frame
    :param file path to dataset which is in json
    :type file_path: str
    :param save: indicates dataset whether is saved into disk. Default is false.
    :type save: bool
    """
    with open(file_path) as json_data:
        return pd.read_json(json_data)


def read_from_dropbox(file_path:str) -> pd.DataFrame:
    """
    Reads file from dropbox
    :return:
    :rtype:
    """
    dbx = dropbox.Dropbox(config.get("DROPBOX", "ACCESS_TOKEN"))
    local_folder = Path('.').cwd().parent / 'data/'
    _, filename = os.path.split(file_path)
    local_file = local_folder.absolute() / filename

    if not os.path.exists(local_file):
        dbx.files_download_to_file(local_file, file_path)
    read_from_json(local_file)

def read_nela_labels(source_name:str,df: pd.DataFrame,score:str = 'default'):
    source = df.loc[df['source'] == source_name]
    if score == 'default':
        return df
    else:
        return source.filter(regex=score + '.*', axis=1)




if __name__ == '__main__':
    read_from_dropbox('/misinfome-martino/google_factcheck_explorer/fact_checking_urls.json')