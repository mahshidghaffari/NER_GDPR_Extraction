# Project Name: Extract Personal Information using hybrid model

# Overview:


This repository contains implementations of different models for Named Entity Recognition (NER). 
The goal of this project is to develop accurate and robust models that can identify and classify 
named entities GDPR related in text data.



# Package Structure:


- LSTM: This package includes the implementation of a Bi-LSTM model for NER. It utilizes bidirectional LSTM layers to capture the contextual information of words in a sentence.

- BERT: This package includes the implementation of a NER model using BERT (Bidirectional Encoder Representations from Transformers). BERT provides contextualized word representations that can enhance the accuracy of the NER system.

- SpaCy: This package includes the implementation of NER using the spaCy library. spaCy offers efficient and pre-trained models for NER, along with additional linguistic features.

- Hybrid Model: This package contains the implementation of a hybrid model that combines the strengths of the Bi-LSTM, BERT, and spaCy models. It aims to achieve improved accuracy and performance by leveraging the complementary features of these models.

- healthData: This package includes the necessary data for training and evaluation. For more detailed information about the data, please refer to the readme file in the "healthdata" package.



# Setup


First for building project run :
```bash
sudo docker-compose up --build
```

To start the service:
```bash
sudo docker-compose up
```

Above command will provide a local URL address which adress the jupyter notebook link to code
and also will provide a token that is the password to the local jupyter notebook
