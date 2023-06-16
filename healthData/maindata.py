# first follow the readme then
# Refrence https://github.com/juand-r/entity-recognition-datasets/blob/master/data/i2b2_2014/README.rst
# https://github.com/Franck-Dernoncourt/NeuroNER/tree/master/neuroner
from brat_to_conII import brat_to_conll,check_brat_annotation_and_text_compatibility


train_in = "/home/jovyan/work/data/health/train"
train_out = "/home/jovyan/work/data/health/train_out.txt"

test_in = "/home/jovyan/work/data/health/test"
test_out = "/home/jovyan/work/data/health/test_out.txt"

valid_in = "/home/jovyan/work/data/health/valid"
valid_out = "/home/jovyan/work/data/health/valid_out.txt"


brat_to_conll(valid_in, valid_out, 'spacy')