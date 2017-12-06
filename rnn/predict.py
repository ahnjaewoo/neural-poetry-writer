# generate a text with given input

import torch
import os

from model import *

# prediction
def predict(model, start_str="A", predict_len=100, temperature=0.8):
	hidden = model.init_hideen(1)
	input_vector = #vecotrize start_str

	predicted = start_str

	return predicted

# generate poem with given input by using saved model 
def generate(model_path, start_str):
