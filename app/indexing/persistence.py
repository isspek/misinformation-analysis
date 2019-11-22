import pandas as pd
import argparse
import json
from app.utils import claimbuster_api
from pathlib import Path
from loguru import logger
import os


def index(data_collection, claimbuster_threshold, output):
    root_dir = Path.cwd().parent
    data_dir = Path('../data')
    df = pd.read_pickle(root_dir / data_dir / data_collection)
    output = root_dir/output
    for index, row in df.iterrows():
        logger.info('Indexing article {feature}', feature=index)
        filename = str(output) + '/claimbuster_results_' + str(index) + '.json'
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        if os.path.exists(filename):
            logger.info('File {feature} exists.', feature = index)
            continue
        try:
            data= {
                'claimbuster_article': claimbuster_api.extract_checkworthy_sentences(article=row['content'],
                                                                                     claimbuster_threshold=claimbuster_threshold),
                'claimbuster_headline': claimbuster_api.extract_checkworthy_sentences(article=row['name'],
                                                                                      claimbuster_threshold=claimbuster_threshold)
            }


            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
        except:
            logger.error(str(index)+' can not be processed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="indexing articles")
    parser.add_argument('--path',
                        '-p',
                        help='path to data collection',
                        default='nela_2018_df.pkl',
                        required=False)

    parser.add_argument('--output',
                        '-o',
                        default='results',
                        help="Output file",
                        required=False)

    parser.add_argument('--claimbuster_threshold',
                        '-t',
                        default=0.4,
                        help="Claimbuster threshold",
                        required=False)

    args = parser.parse_args()
    index(data_collection=args.path, claimbuster_threshold=args.claimbuster_threshold, output=args.output)
