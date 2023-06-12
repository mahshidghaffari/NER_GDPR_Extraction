import numpy as np
import pandas as pd
import os
from subprocess import check_output
import tensorflow as tf
from keras.models import Model
from tensorflow.keras.layers import Input
# from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from tensorflow.keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from LstmM.lstmFun import encoding
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


class LstmModel:

    def __init__(self, train_df, test_df):
        self.y_pred = None
        self.historyLSTM = None
        self.model = None
        self.input_df = None
        self.train_data = train_df
        self.test_data = test_df
        self.tags = list(train_df["tag"].unique())

        self.x_train, self.y_train, self.train_maxlen, self.train_n_words, self.train_n_tag, self.train_tag, self.tag2idx_train = encoding(self.train_data)
        self.x_test, self.y_test, self.test_maxlen, self.test_n_words, self.test_n_tag, self.test_tag, self.tag2idx_test = encoding(self.test_data)
        self.maxlen = max(self.test_maxlen, self.train_maxlen)

    def print_variables(self):
        print("x_train shape:", len(self.x_train))
        print("y_train shape:", len(self.y_train))
        print("train_maxlen:", self.train_maxlen)
        print("train_n_words:", self.train_n_words)
        print("train_n_tag:", self.train_n_tag)

        print("x_test shape:", len(self.x_test))
        print("y_test shape:", len(self.y_test))
        print("test_maxlen:", self.test_maxlen)
        print("test_n_words:", self.test_n_words)
        print("test_n_tag:", self.test_tag)
        print("Model Summary", self.model.summary())

    def train_model(self):
        input_sequence = Input(shape=(self.maxlen,), name='input_sequence')
        embedding_layer = Embedding(input_dim=self.train_n_words, output_dim=self.maxlen, input_length=self.maxlen)(
            input_sequence)
        dropout_layer = Dropout(0.1)(embedding_layer)
        lstm_layer = Bidirectional(LSTM(units=100, return_sequences=True, recurrent_dropout=0.1))(dropout_layer)
        output_layer = TimeDistributed(Dense(self.train_n_tag, activation="softmax"))(lstm_layer)

        model = Model(input_sequence, output_layer)
        model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

        history = model.fit(self.x_train, np.array(self.y_train), batch_size=32, epochs=40, verbose=1)
        self.historyLSTM = history
        self.model = model

    def save_model(self):
        self.model.save("data/output/LSTM_")

    def read_model(self, dir):
        self.model = tf.keras.models.load_model(dir)


    def general_evaluation(self):
        print(self.x_test.shape)
        print(len(self.y_test))
        loss, accuracy = self.model.evaluate(self.x_test, np.array(self.y_test))
        print("Loss: {:.4f}".format(loss))
        print("Accuracy: {:.2f}%".format(accuracy * 100))

        self.y_pred = self.model.predict(self.x_test)
        y_pred_indices = np.argmax(self.y_pred, axis=-1)

        # Flatten the true and predicted labels
        y_true_flattened = np.argmax(self.y_test, axis=-1).flatten()
        y_pred_flattened = y_pred_indices.flatten()

        # Calculate F1 score
        f1 = f1_score(y_true_flattened, y_pred_flattened, average='weighted')

        # Calculate accuracy
        accuracy = accuracy_score(y_true_flattened, y_pred_flattened)

        # Print the evaluation metrics
        print("F1 Score:", f1)
        print("Accuracy:", accuracy)

    def tag_evaluation(self):

        y_true_flattened = np.argmax(self.y_test, axis=-1).flatten()
        y_pred_flattened = np.argmax(self.y_pred, axis=-1).flatten()

        # Get the list of unique tags
        unique_tags = list(set(self.tags))
        tag2idx = {t: i for i, t in enumerate(unique_tags)}
        # Initialize dictionaries to store evaluation metrics per tag
        f1_per_tag = {}
        accuracy_per_tag = {}

        for tag in unique_tags:
            mask = (y_true_flattened == tag2idx[tag])
            y_true_tag = y_true_flattened[mask]
            y_pred_tag = y_pred_flattened[mask]

            # Calculate F1 score
            f1 = f1_score(y_true_tag, y_pred_tag, average='weighted')

            # Calculate accuracy
            accuracy = accuracy_score(y_true_tag, y_pred_tag)

            f1_per_tag[tag] = f1
            accuracy_per_tag[tag] = accuracy

        # Print the evaluation metrics per tag
        for tag in unique_tags:
            print("Tag:", tag)
            print("F1 Score:", f1_per_tag[tag])
            print("Accuracy:", accuracy_per_tag[tag])
            print("_______________________")
