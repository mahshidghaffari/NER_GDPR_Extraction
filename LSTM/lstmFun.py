def get_sentences(dataset):
    n_sent = 1
    grouped = dataset.groupby("sentence_idx").apply(lambda s: [(w, t) for w, t in zip(s["word"].values.tolist(),
                                                                                      s["tag"].values.tolist())])
    sentences = [s for s in grouped]

    def get_next():
        nonlocal n_sent
        try:
            s = grouped["Sentence: {}".format(n_sent)]
            n_sent += 1
            return s
        except:
            return None

    return sentences, get_next


def get_max_len(sentences):
    return max([len(s) for s in sentences])


def add_sentence_id_column(dataset):
    sentence_idx = 1
    sentence_indices = []
    for word in dataset['word']:
        sentence_indices.append(sentence_idx)
        if word == '.':
            sentence_idx += 1
    dataset.insert(0, 'sentence_idx', sentence_indices)
    return dataset