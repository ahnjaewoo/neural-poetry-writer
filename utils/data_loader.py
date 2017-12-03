import codecs
import numpy as np

# 여러 파일에 나뉘어져있는 데이터를 한 파일로 합치기 위한 모듈
# clean : 저장 할 파일을 초기화
# gather('a.txt', 'b.txt', ...) : args로 주어진 파일들을 읽어 대상파일로 저장
# thought connect, append, cut mode is not this module's scope.
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
# connect or not is not this module's scope
# add or sub is this module's scope
class batch_maker():
    def __init__(self, strided=False, mode='add'):
        self.strided = strided
        self.mode = mode
    #
    def make_normal_batch(self, source, start, end, seq_len):
        return
    def make_stride_batch(self, source, start, end, seq_len, stride = 2):
        return

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