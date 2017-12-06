# Training functions for RNN model
import random
import torch
import torch.nn as nn
import time
import math
import os
from torch.autograd import Variable

# gat one mini batch from total data randomly
def random_batch(data_batch):
	index = random.randint(0, len(data_batch) - 1)
	return data_batch[index]

# make a mini batch
def random_training_set(data_batch, sequence_len, batch_size):
	X = torch.LongTensor(batch_size, sequence_len-1)
	Y = torch.LongTensor(batch_size, sequence_len-1)
	
	for batch_iter in range(batch_size):
		batch = random_batch(data_batch)
		sequence = batch[batch_iter]
		# takes all characters in one sequence as an input
		X[batch_iter] = torch.from_numpy(sequence[:-1])
		# all characters (except the first one) in one sequence are expected output
		Y[batch_iter] = torch.from_numpy(sequence[1:])

	X = Variable(X)
	Y = Variable(Y)
  
	return X, Y

# training function
# given a model, optimizer, loss function adjust the params
def train(model, optimizer, criterion, sequence_len, batch_size, X, Y):
	hidden = model.init_hidden(batch_size)
	model.zero_grad()
	loss = 0

	for c in range(sequence_len-1):
		output, hidden = model(X[:,c], hidden)
		loss += criterion(output.view(batch_size, -1), Y[:,c])

	loss.backward()
	optimizer.step()

	return loss.data[0] / sequence_len

def time_since(since):
    s = time.time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

# save trained model
def save(model, file_name):
  save_filename = os.path.splitext(os.path.basename(file_name))[0] + '.pt'
  torch.save(model, save_filename)
  print('Saved as %s' % save_filename)
