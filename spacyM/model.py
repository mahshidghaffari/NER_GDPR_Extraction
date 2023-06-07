# # import lib
import spacy
from spacy import displacy
import pandas as pd

from spacy.matcher import Matcher
from spacy.tokens import Span


nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

class SpacyModel:
    def __init__(self, data):
        # self.doc_nlp = nlp(data)
        self.doc_nlp = data

    def test(self):
        return "test"
