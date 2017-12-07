import codecs
import numpy as np
import re

class data_cutter():
	def __init__(self, control_dir):
		self.control_dir = control_dir
		self.custom_accept_from = ['&NewLine;']
		self.custom_accept_to = ['\n']
		self.custom_disallow_from = list()
		self.fixed_from = [ch for ch in 'QWERTYUIOPASDFGHJKLZXCVBNM']
		self.fixed_to = [ch for ch in 'qwertyuiopasdfghjklzxcvbnm']
		f = codecs.open(self.control_dir +'/'+ "unaccept.txt", "r", 'utf-8')
		text = f.read()
		for ch in text:
			self.custom_disallow_from.append(ch)
		f.close()
		self.custom_rule_load()
	def custom_rule_load(self):
		# set accept
		f = codecs.open(self.control_dir +'/'+ "accept.txt", "r", 'utf-8')
		lines = f.readlines()
		t_accept_from = list()
		t_accept_to = list()
		idx = 0
		tok = ''
		for text in lines:
			if(idx%2 == 0):
				tok = text[:-1]
			else:
				# split text
				s_text = text[:-1].split()
				# add each entry
				for entry in s_text:
					t_accept_from.append(entry)
					t_accept_to.append(tok)
			idx += 1
		self.custom_accept_from = t_accept_from
		self.custom_accept_to = t_accept_to
		f.close()
		# set disallow
		f = codecs.open(self.control_dir +'/'+ "disallow.txt", "r", 'utf-8')
		lines = f.readlines()
		t_disallow_from = list()
		for text in lines:
			s_text = text[:-1].split()
			t_disallow_from.extend(s_text)
		self.custom_disallow_from.extend(t_disallow_from)
		f.close()
	def custom_accpet(self, text):
		accept_from = self.custom_accept_from
		accept_to = self.custom_accept_to
		for i in range(0, len(accept_from)):
			text = text.replace(accept_from[i], accept_to[i])
		return text
	def custom_disallow(self, text):
		disallow_from = self.custom_disallow_from
		for i in range(0, len(disallow_from)):
			text = text.replace(disallow_from[i], ' ')
		return text
	def merge_space(self, text):
		text = re.sub('[ \t]+',' ',text)
		text = re.sub(' \n','\n',text)
		text = re.sub('\n ','\n',text)
		return text
	def fixed_accpet(self, text):
		accept_from = self.fixed_from
		accept_to = self.fixed_to
		for i in range(0, len(accept_from)):
			text = text.replace(accept_from[i], accept_to[i])
		return text
	def data_cut(self, text):
		# HTML filter / custom filter
		text = self.custom_accpet(text)
		text = self.custom_disallow(text)
		# merge space
		text = self.merge_space(text)
		# tolower
		text = self.fixed_accpet(text)
		return text