import urllib
import requests
import json
from loguru import logger
from app.conf import config
from app.text_processor import preprocessing


CLAIMBUSTER_ENDPOINT = config.config.get("API","claimbuster")
UTF_CODE = 'utf-8'


def extract_checkworthy_sentences(article, claimbuster_threshold):
    splitted_article = preprocessing.split_sentences(article)
    avg_checkworthy_sentences = 0
    checkworthy_sentences = []
    logger.info('Find checkworthy claims in text.')
    for sentence in splitted_article:
        value = _compute_checkworthy(claimbuster_threshold, sentence)
        if value > claimbuster_threshold:
            avg_checkworthy_sentences += 1
            checkworthy_sentences.append([sentence,value])
    logger.info('Checkworthy claims are extracted.')
    return {
        'avg_checkworthy_sentences': avg_checkworthy_sentences / len(splitted_article),
        'checkworthy_sentences': checkworthy_sentences,
        'num_of_sentences': len(splitted_article)
    }


def _compute_checkworthy(claimbuster_threshold, sentence):
    query = CLAIMBUSTER_ENDPOINT + urllib.parse.quote(sentence)
    value = 0

    try:
        logger.info('Request claimbuster api')
        response = requests.get(query)
        response = json.loads(response.content.decode(UTF_CODE))
        logger.info('Response: {response}',response=response)
        value = float(response['results'][0]['score'])
        logger.info('Response from claimbuster is returned.')
        return value
    except:
        logger.error("Couldn't query")
