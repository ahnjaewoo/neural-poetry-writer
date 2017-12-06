import codecs
import numpy as np

# represent character as a number, vector
# 
class code_book():
	def __init__(self, midfile_dir):
		self.vector_size = 0
		self.codes = dict()
		self.invert_codes = list()

		self.midfile_dir = midfile_dir
	# gather - if given character is unknown, create mapping and add it to codes
	# gather fucntion changes : now count occurence
	def gather(self, character):
		if(self.codes.get(character) == None):
			self.codes[character] = 1
		else:
			self.codes[character] += 1
	def sort_codes(self):
		codes = self.codes
		invert_codes = self.invert_codes
		codes_list = sorted(codes, key=lambda k : codes[k], reverse=True)
		codes_temp = dict()
		idx = 0
		for ch in codes_list:
			codes_temp[ch] = idx
			invert_codes.append(ch)
			idx += 1
		self.codes = codes_temp
		self.invert_codes = invert_codes
		self.vector_size = idx
	# save to a file with specific format, use codes
	def save_to(self, filename):
		f = codecs.open(self.midfile_dir +'/'+ filename, "w", 'utf-8')
		codes = self.codes
		for key, value in codes.items():
			f.write(key)
		f.close()
	# load from a file of format assumption, form codes
	def load_from(self, filename):
		self.codes.clear()
		self.invert_codes = []
		f = codecs.open(self.midfile_dir +'/'+ filename, "r", 'utf-8')
		text = f.read()
		idx = 0
		for ch in text:
			self.codes[ch] = idx
			self.invert_codes.append(ch)
			idx += 1
		self.vector_size = idx
		f.close()

	def get_number(self, text):
		number = [self.codes[ch] for ch in text]
		return number
	def get_number_batch(self, batch):
		number_batch = list()
		for seq in batch:
			number_batch.append(self.get_number(seq))
		return number_batch
	def get_number_batchs(self, batchs):
		number_batchs = list()
		for batch in batchs:
			number_batchs.append(self.get_number_batch(batch))
		return number_batchs
	
	def get_string(self, number_text):
		text = ""
		for nch in number_text:
			text += self.invert_codes[nch]
		return text
	def get_string_batch(self, number_batch):
		batch = list()
		for number_seq in number_batch:
			batch.append(self.get_string(number_seq))
		return batch
	def get_string_batchs(self, np_batchs):
		batchs = list()
		number_batchs = np_batchs.tolist()
		for number_batch in number_batchs:
			batchs.append(self.get_string_batch(number_batch))
		return batchs

	# get numpy vector representation of string, based on codes
	def get_vectors(self, text):
		text_num = get_numbers(text)
		vectors = np.zeros((len(text), self.vector_size))
		for i in range(len(text)):
			vectors[i][text_num[i]] = 1
		return vectors
	# length of a vector (=vector size)
	def size(self):
		return self.vector_size
	# debug purpose only
	def debug_print(self):
		print(self.vector_size)
		print(self.codes)
		