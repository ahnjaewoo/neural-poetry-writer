# RNN model

import torch
import torch.nn as nn
from torch.autograd import Variable

class RNN(nn.Module):
	def __init__(self, input_size, hidden_size, output_size, n_layers=1):
		super(RNN, self).__init__()
		self.input_size = input_size
		self.hidden_size = hidden_size
		self.output_size = output_size
		self.n_layers = n_layers

		self.encoder = nn.Embedding(input_size, hidden_size)
		self.lstm = nn.LSTM(hidden_size, hidden_size, n_layers)
		self.decoder = nn.Linear(hidden_size, output_size)

	def forward(self, input, hidden):
		batch_size = input.size(0)
		encoded = self.encoder(input)
		output, hidden = self.lstm(encoded.view(1, batch_size, -1), hidden)
		output = self.decoder(output.view(batch_size, -1))


	def init_hidden(self, batch_size):
		return (Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size)),
				Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size)))