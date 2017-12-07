# generate a text with given input
import torch
import os
import numpy as np

from torch.autograd import Variable

# prediction
def predict(model, start_sequence, predict_len=100, temperature=0.8):
	hidden = model.init_hidden(1)
	sequence_len = len(start_sequence)
 
	X = torch.LongTensor(start_sequence).unsqueeze(0)
	X = Variable(X)

	predicted = np.array(start_sequence).flatten().tolist()
	# build up hidden states
	for i in range(sequence_len-1):
		_, hidden = model(X[:,i], hidden)
	# generate new character with last character of given sequence
	X = X[:,-1]

	# generate a sequence of characters
	for i in range(predict_len):
		output, hidden = model(X, hidden)

		# sample from the network as a multinomial distribution
		output_dist = output.data.view(-1).div(temperature).exp()
		top_vector = torch.multinomial(output_dist, 1)[0]

		# append generated vector to sequence
		predicted.append(top_vector) 
		# output is the next input
		X = torch.LongTensor([top_vector]).unsqueeze(0)
		X = Variable(X)

	# return the generated sequence except input
	return predicted
