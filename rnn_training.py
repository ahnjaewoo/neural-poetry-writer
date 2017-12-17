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

# data loader
loader = data_loader(sequence_len, batch_size, rawdata_dir, middata_dir)
loader.load()

# load functionality check
cb = loader.cb
data_batch = loader.np_batchs

# Training New Model

# Model Params
input_size = cb.size()
hidden_size = 512
output_size = cb.size()
n_layers = 3
dropout = 0.25
# Model
#decoder = RNN(input_size, hidden_size, output_size, n_layers, dropout)

# Training Exist Model
model_name = "rnn_model_result_final.pt"
save_model_name = model_name.split('.')[0]
decoder = torch.load(model_dir + "/" + model_name)

# Training Script
# Hyper Params
lr = 0.003
n_epochs = -1
print_cycle = 10
save_cycle = 10000
start_sequence = cb.get_number_batch("apple")

optimizer = torch.optim.Adam(decoder.parameters(), lr)
criterion = nn.CrossEntropyLoss()
start = time.time()

try:
    if (n_epochs == -1):
        epoch = 0
        while (True):
            epoch += 1
            print(epoch)
            loss = train(decoder, optimizer, criterion, sequence_len, batch_size , *random_training_set(data_batch, sequence_len, batch_size))
            
            if epoch % print_cycle == 0:
                print('[Time : %s, Epoach : (%d), Loss : %.4f]' % (time_since(start), epoch, loss))
                print(cb.get_string(predict(decoder, start_sequence, 100)))
            if (epoch % save_cycle == 0):
	        save(decoder, "./"+model_dir+"/"+save_model_name+"-"+str(model_num))
		print("Save %d model" % (model_num))

    else :
        print("Training for %d epochs..." % n_epochs)
        for epoch in range(1, n_epochs + 1):
            loss = train(decoder, optimizer, criterion, sequence_len, batch_size , *random_training_set(data_batch, sequence_len, batch_size))

            if epoch % print_cycle == 0:
                print('[Time : %s, Epoach : (%d), Loss : %.4f]' % (time_since(start), epoch, loss))
                print(cb.get_string(predict(decoder, start_sequence, 100)))

        print("Learning end.. Saving...")
        f = open("./" + poem_dir + "/poem_result.txt", 'w')
        predicted = predict(decoder, start_sequence, 1000)
        f.write(cb.get_string(predicted))
        save(decoder, "./"+model_dir+"/"+save_model_name)
        f.close()
        
except KeyboardInterrupt:
    print("Saving before quit...")
    save(decoder, "./"+model_dir+"/"+save_model_name)
    
except :
    print("Learning Failure!! Saving before quit...")
    save(decoder, "./"+model_dir+"/"+save_model_name)
