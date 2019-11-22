import nltk
from loguru import logger


def split_sentences(article):
    logger.debug("splitting article before \n {feature}", feature=article)
    text_blocks = []
    sent_text = nltk.sent_tokenize(article)
    for sentence in sent_text:
        text_blocks.append(sentence)
    logger.debug("after \n {feature}", feature=sent_text)
    return text_blocks
