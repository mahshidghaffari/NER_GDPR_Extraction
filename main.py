import pandas as pd
# from LstmM.model import LstmModel
# from spacyM.model import SpacyModel
import splitData


data = pd.read_csv("data/health/relabel_full_i2b2_data.csv")
splitData.split_data(data, "data/health/", "i2b2")

# data = "peter Parker has bachelor degree and "
# model = SpacyModel(data)
#

# train_data = pd.read_csv("data/label_data/ner_train_data.csv")
# test_data = pd.read_csv("data/label_data/ner_test_data.csv")
# lstm_40_epochs = 'data/output/LSTM_'
# lstm_1_epochs = 'data/output/LSTM_1batch'

# LSTM MODEL: Traind and save the model
# LSTM_model = LstmModel(train_data, test_data)
# LSTM_model.print_variables()
# LSTM_model.train_model()
# LSTM_model.save_model()

# LSTM MODEL:  Evaluation in general and per tag

# LSTM_model_evaluation = LstmModel(train_data, test_data);
# LSTM_model_evaluation.read_model(lstm_1_epochs)
# LSTM_model_evaluation.print_variables();
# LSTM_model_evaluation.general_evaluation()
# LSTM_model_evaluation.tag_evaluation()