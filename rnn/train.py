# Training phase with RNN model
import random
import torch
import torch.nn as nn
import time
import os
from torch.autograd import Variable

from model import *
from predict import *

# get a sequence in a data file randomly
def random_sequence (sequence_len):
	start_index = random.randint(0, data_len - sequence_len)
	end_index = start_index + sequence_len
	return data[start_index:end_index]

# make a mini batch
def random_training_set (sequence_len, batch_size):
	X = torch.LongTensor(batch_size, sequence_len)
    Y = torch.LongTensor(batch_size, sequence_len)
    for batch_iter in range(batch_size):
    	sequence = random_sequence(sequence_len)
        # takes all characters in one sequence as an input
        X[batch_iter] = sequence 
        # all characters (except the first one) in one sequence are expected output
        X[batch_iter] = # TODO 

    X = Variable(X)
    Y = Variable(Y)
    
    return X, Y

# save trained model
def save(model, file_name):
    save_filename = os.path.splitext(os.path.basename(file_name))[0] + '.pt'
    torch.save(model, save_filename)
    print('Saved as %s' % save_filename)

# Training Phase 
def train_run (input_size, hidden_size, output_size, sequence_len, batch_size=1, n_layers=1, n_epochs=-1, cycle=100)
	decoder = RNN(input_size, hidden_size, output_size, n_layers=1)
	start = time.time()
	all_losses = []
	loss_avg = 0

	# Data loader -> Train

	try:
		if (n_epochs = -1):
			epoch = 0
			while (true):
				epoch++
				loss = train(*random_training_set(sequence_len, batch_size))
      	loss_avg += loss

      	if epoch % cycle == 0:
          print('[Time : %s, Epoach : (%d), Loss : %.4f]' % (time_since(start), epoch, loss))
          save()
          print(generate(decoder, 'Wh', 100, cuda=args.cuda), '\n')

		else :
    	print("Training for %d epochs..." % n_epochs)
    	for epoch in tqdm(range(1, args.n_epochs + 1)):
	    	loss = train(*random_training_set(args.chunk_len, args.batch_size))
	    	loss_avg += loss

	    	if epoch % args.print_every == 0:
	        	print('[%s (%d %d%%) %.4f]' % (time_since(start), epoch, epoch / args.n_epochs * 100, loss))
	        	print(generate(decoder, 'Wh', 100, cuda=args.cuda), '\n')

    	print("Saving...")
    	save()

	except KeyboardInterrupt:
    	print("Saving before quit...")
    	save()


