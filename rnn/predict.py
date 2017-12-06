# generate a text with given input
import torch
import os

# prediction
def predict(model, start_sequence, predict_len=100, temperature=0.8):
	hidden = model.init_hideen(1)
	sequence_len = len(start_sequence)

	X = torch.LongTensor(sequence_len)
	X = torch.from_numpy(start_sequence)
	X = Variable(X)

	predicted = start_sequence

	# build up hidden states
	for i in range(sequence_len-1):
		_, hidden = model(X[:,i], hidden)

	X = X[:, -1]

	for i in range(predict_len):
		output, hidden = model(X, hidden)
	for c in range(len())
	return predicted
