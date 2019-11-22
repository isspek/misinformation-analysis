import spacy
from typing import List

ADJ = "ADJ"
NOUN = "NOUN"
PROPN = "PROPN"
VERB = "VERB"

class NLPTool:
    def __init__(self, lang: str):
        self.tool = spacy.load(lang)

def get_pos_tags(self,tool, doc: str) -> List[str]:
    doc = tool(doc)
    lemmas = []
    adjectives = []
    nouns = []
    verbs = []

    for token in doc:
        lemmas.append(token.lemma_)
        if token.pos_ == ADJ:
            adjectives.append(token.lemma_)
        if token.pos_ == NOUN or token.pos_ == PROPN:
            nouns.append(token.lemma_)
        if token.pos_ == VERB:
            verbs.append(token.lemma_)

    return lemmas, adjectives, nouns, verbs


