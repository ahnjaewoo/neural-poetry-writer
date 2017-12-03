import codecs
import numpy as np

# 여러 파일에 나뉘어져있는 데이터를 한 파일로 합치기 위한 모듈
# clean : 저장 할 파일을 초기화
# gather('a.txt', 'b.txt', ...) : args로 주어진 파일들을 읽어 대상파일로 저장
# (drop/add), (normal/stride), (whole/one) mode is not this module's scope.
class data_gatherer():
	def __init__(self, encoding='utf-8'):
		self.poem_set = 'poem_set.txt'
		self.title_set = 'title_set.txt'
		self.encoding = encoding
	def path_parse(self, text):
		title = list()
		data = list()
		start = text.find('POEM_TITLE\n')
		while(start != -1):
			text = text[start+len('POEM_TITLE\n'):]
			middle = text.find('POEM_DATA\n')
			start = text.find('POEM_TITLE\n')
			
			title.append(text[:middle-1])
			if(start == -1):
				data.append(text[middle+len('POEM_DATA\n'):-1])
			else:
				data.append(text[middle+len('POEM_DATA\n'):start-1])
		return title, data
	def clean(self):
		f = codecs.open(self.poem_set, "w", self.encoding)
		f.close()
		f = codecs.open(self.title_set, "w", self.encoding)
		f.close()
	def gather(self, path_list):
		f1 = codecs.open(self.poem_set, "a", self.encoding)
		f3 = codecs.open(self.title_set, "a", self.encoding)
		for path in path_list:
			with codecs.open(path, "r", encoding=self.encoding) as f2:
				text = f2.read()
				# do text processing
				titles, data = self.path_parse(text)
				for i in range(len(data)):
					datum = data[i]
					title = titles[i]
					title_pos = len(datum)
					if(datum[-1]!='\n'):
						datum += '\n'
						title_pos += 1
					f1.write(datum)
					f3.write(title+'\n'+str(title_pos)+'\n')
			f2.close()
		f1.close()
		f3.close()

# 배치 생성 모듈
# drop/add
# normal/stride
# whole/one -------------------------------------> TODO
class batch_maker():
	def __init__(self, batch_size=20, seq_len=20, stride=2, mode='add'):
		self.stride = stride
		self.mode = mode
		self.seq_len = seq_len
		self.batch_size = batch_size
	# drop leftover based on sequence length
	def dropped_text(self, text):
		seq_len = self.seq_len

		text_len = len(text)
		leftover = text_len % seq_len
		text_len = len(text)
		if(leftover != 0):
			text = text[:text_len - leftover]
		return text
	# pad not filled area based on sequence length, using front of text
	def added_text(self, text):
		seq_len = self.seq_len

		text_len = len(text)
		leftover = text_len % seq_len
		add_count = seq_len - leftover
		if(add_count != 0):
			text = text + text[:add_count]
		return text
	# return strided text area based on sequence length, if limit reached, return None	
	def seqs_stride_get(self, text, stride_idx, text_len):
		seq_len = self.seq_len

		if(text_len >= stride_idx + seq_len):
			return text[stride_idx:stride_idx + seq_len]
		else:
			return None

	# make sequences from source
	def seqs_normal(self, source, start, end):
		seq_len = self.seq_len
		mode = self.mode

		text = source[start:end]
		if(len(text) < seq_len):
			# 1 append routine
			text = added_text(text)
			prd.append(text)
		else:
			# 2 drop/append routine
			if(mode == 'add'):
				text = added_text(text)
			else:
				text = dropped_text(text)
			# split by seq_len
			prd.append(text[0+idx:seq_len+idx]) for idx in range(0, len(text), seq_len)
		return prd
	# make sequences from source, strided method
	def seqs_stride(self, source, start, end):
		seq_len = self.seq_len

		text = source[start:end]
		prd = list()
		if(len(text) < seq_len):
			# 1 append routine
			text = added_text(text)
			prd.append(text)
		else:
			text_len = len(text)
			stride_idx = 0
			while((seq = seqs_stride_get(text, stride_idx, text_len)) != None):
				# add seq to prd
				prd.append(seq)
				# slide
				stride_idx += stride
		return prd

	def make_batchs(self):
		count = 0
		batchs = list()
		batch = list()
		# get seqs by seqs_ function
		for seq in seqs:
			if(count >= batch_size):
				count = 0
				batchs.append(batch)
				batch = list()
			batch.append(seq)
			count += 1
		if(count >= batch_size):
			batchs.append(batch)
		return batchs
	def batchs_poem():

# 데이터를 로드, 전처리, 배치 생성을 위함
# https://github.com/sherjilozair/char-rnn-tensorflow/blob/master/utils.py
# https://chunml.github.io/ChunML.github.io/project/Creating-Text-Generator-Using-Recurrent-Neural-Network/
# 참조
class data_loader():
	def __init__(self, seq_len, batch, poem_collection="poem_collection.txt", encoding='utf-8'):
		self.poem_collection = poem_collection
		self.seq_len = seq_len
		self.batch = batch
		self.encoding = encoding
	def data_preprocess():
		return
	def data_load():
		return
	def make_batch():
		return