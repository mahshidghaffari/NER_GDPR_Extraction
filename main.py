import pandas as pd
from LstmM.model import LstmModel
# from spacyM.model import SpacyModel
import splitData

# data = "peter Parker has bachelor degree and "
# model = SpacyModel(data)
#

train_data = pd.read_csv("data/label_data/ner_train_data.csv")
test_data = pd.read_csv("data/label_data/ner_test_data.csv")

# LSTM MODEL
LSTM_model = LstmModel(train_data, test_data)
LSTM_model.print_variables()
LSTM_model.train_model()
LSTM_model.save_model()

# LSTM MODEL Evaluation