# # import lib
from random import random
from spacy.training.example import Example
import spacy
from spacy import displacy
import pandas as pd
from spacy.util import minibatch, compounding

from spacy.matcher import Matcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)


def reformat_data_spacy_format(data):
    grouped = data.groupby("sentence_idx").apply(
        lambda s: [(w, t) for w, t in zip(s["word"].values.tolist(), s["tag"].values.tolist())])
    sentences = [s for s in grouped]
    data_encoded = []
    for s in sentences:
        full_s = ""
        start_index = 0
        last_index = 0
        index_counter = 0
        entities = []
        for w in s:
            full_s += str(w[0]) + " "
            entities.append((index_counter, index_counter + len(str(w[0])), w[1]))
            index_counter += len(str(w[0])) + 1
        data_encoded.append((full_s, {"entities": entities}))

    return data_encoded


class SpacyModel:
    def __init__(self, train_df, test_df):
        self.train_data = reformat_data_spacy_format(train_df)
        self.test_data = reformat_data_spacy_format(test_df)

        # Initialize a new blank spaCy model
        self.nlp = spacy.load("en_core_web_sm")
        self.ner = nlp.get_pipe("ner")

        # Add custom tags to the NER pipeline
        self.add_to_pip()

        # Disable unnecessary pipeline components
        pipe_exceptions = ["ner"]
        self.unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

    def add_to_pip(self):

        for _, annotations in self.train_data:
            for entity in annotations.get("entities"):
                self.ner.add_label(entity[2])

    def train_spacy(self):
        with self.nlp.disable_pipes():
            # Training iterations...
            for iteration in range(30):
                # Shuffle training examples before every iteration
                random.shuffle(self.train_data)
                losses = {}
                examples = []

                # Create Example objects from training data
                for text, annotation in self.train_data:
                    doc = self.nlp.make_doc(text)
                    example = Example.from_dict(doc, annotation)
                    examples.append(example)

                # Batch up the examples using spaCy's minibatch
                batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))
                for batch in batches:
                    self.nlp.update(batch, drop=0.5, losses=losses)

                print("Losses:", losses)

    def save_model(self, dir):
        output_dir = "work/data/output/spacyModel"
        self.nlp.to_disk(output_dir)
