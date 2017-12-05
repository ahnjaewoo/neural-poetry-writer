# Training phase with RNN model

import torch
import torch.nn as nn
from torch.autograd import Variable

from model import *

def random_training_set(sequence_len, batch_size):
	#

	input = torch.LongTensor(batch_size, sequence_len)
    output = torch.LongTensor(batch_size, sequence_len)
    for batch_iter in range(batch_size):

    for bi in range(batch_size):
        start_index = random.randint(0, file_len - chunk_len)
        end_index = start_index + chunk_len + 1
        chunk = file[start_index:end_index]
        # takes all characters in one sequence as an input
        input_data[bi] = char_tensor(chunk[:-1])
        # all characters (except the first one) in one sequecne are expected output
        target[bi] = char_tensor(chunk[1:]) 
    inp = Variable(inp)
    target = Variable(target)
    if args.cuda:
        inp = inp.cuda()
        target = target.cuda()
    return inp, target