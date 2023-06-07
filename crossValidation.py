import csv
from subprocess import check_output
import pandas as pd
from sklearn.model_selection import train_test_split


def cross_validation(data, output_dir, output_name):
    # Group data by sentences and split data w.r.t the sentence structure
    grouped = data.groupby("sentence_idx").apply(lambda s: [(w, t) for w, t in zip(s["word"].values.tolist(),
                                                                                   s["tag"].values.tolist())])
    grouped_df = pd.DataFrame(grouped, columns=["sentences"])
    train_sentences, test_sentences = train_test_split(grouped_df, test_size=0.2, random_state=42)
    train_sentences = train_sentences['sentences']
    test_sentences = test_sentences["sentences"]

    # Create empty lists for the train columns
    train_sentence_id = []
    train_words = []
    train_tags = []

    # Iterate over the grouped train data
    for sentence_idx, sentence_data in train_sentences.items():
        for word, tag in sentence_data:
            train_sentence_id.append(sentence_idx)
            train_words.append(word)
            train_tags.append(tag)

    train_data = pd.DataFrame({"train_sentence_id": train_sentence_id, "word": train_words, "tag": train_tags})

    train_data.to_csv(output_dir + output_name + "_train_data.csv", index=False)

    # Create empty lists for test columns
    test_sentence_id = []
    test_words = []
    test_tags = []

    # Iterate over the grouped test data
    for sentence_idx, sentence_data in test_sentences.items():
        for word, tag in sentence_data:
            test_sentence_id.append(sentence_idx)
            test_words.append(word)
            test_tags.append(tag)

    test_data = pd.DataFrame({"test_sentence_id": train_sentence_id, "word": train_words, "tag": train_tags})

    test_data.to_csv(output_dir + output_name + "_test_data.csv", index=False)
