from rnn.model import *
from rnn.train import *
from rnn.predict import *
from utils.data_loader import *

# Hyper params
batch_size = 100
sequence_len = 400
# Data path
rawdata_dir = 'raw_data/data'
middata_dir = 'mid_data'
poem_dir = "poem_result"
model_dir = "rnn_models"

# loda data with preprocessing
loader = data_loader(sequence_len, batch_size, rawdata_dir, middata_dir)
loader.file_preprocess()
loader.save()
