
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
def get_sentences(dataset):
    n_sent = 1
    # print(dataset[0])
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
def encoding(data):
    # dframe = lstmFun.add_sentence_id_column(self.data)
    sentences, get_next = get_sentences(data)
    maxlen = get_max_len(sentences)
    print('Maximum sequence length:', maxlen)

    words = list(set(data["word"].values))
    words.append("ENDPAD")
    n_words = len(words);

    tags = list(set(data["tag"].values))
    n_tags = len(tags)

    word2idx = {w: i for i, w in enumerate(words)}
    tag2idx = {t: i for i, t in enumerate(tags)}

    x = [[word2idx[w[0]] for w in s] for s in sentences]
    x = pad_sequences(maxlen=maxlen, sequences=x, padding="post", value=n_words - 1)

    y = [[tag2idx[w[1]] for w in s] for s in sentences]
    y = pad_sequences(maxlen=maxlen, sequences=y, padding="post", value=tag2idx["O"])
    y = [to_categorical(i, num_classes=n_tags) for i in y]
    return x, y, maxlen, n_words, n_tags


def test():
    return "hello"
