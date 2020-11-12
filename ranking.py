import numpy as np
class Ranker:
    def __init__(self,index):
        self.index = index
        self.D = index.documentWords
        self.d_avg = np.array(self.D).mean()
    def TDmatrix(self,query):
        TD={}
        for word in query:
            for doc,frequency in self.index[word]:
                TD[(word,doc)] = frequency
        return TD