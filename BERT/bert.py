from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

bert_tokenizer = AutoTokenizer.from_pretrained('dslim/bert-large-NER')
bert_model = AutoModelForTokenClassification.from_pretrained('dslim/bert-large-NER')


def identify(names_string: str) -> dict:
    """A function that identifies NERs using BERT"""
    nlp = pipeline('ner', model=bert_model, tokenizer=bert_tokenizer)
    return nlp(names_string)


