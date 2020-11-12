import numpy as np
from collections import defaultdict
from math import log
from nltk import word_tokenize
class BM25Ranker:
    def __init__(self,index,N,k,b):
        self.index = index
        self.D = index.documentWords
        self.d_avg = np.array(self.D).mean()
        self.totalDocs = N
        self.k=k
        self.b=b
    def getTDmatrix(self,query):
        TD={}
        for word in query:
            for doc,frequency in self.index[word]:
                TD[(word,doc)] = frequency
        return TD
    def getIDF(self,query,TD):
        IDF=defaultdict(0)
        for q in query:
            Nq=0
            for word,_ in TD.keys():
                if(q==word):
                    Nq+=1
            IDF[q]=log(1+((self.totalDocs-Nq+0.5)/(Nq+0.5)))
        return IDF
    def getTermFrequency(self,query,TD):
        TF = defaultdict(0)
        for q in query:
            for word,_ in TD.keys():
                if(q==word):
                    TF[q]+=1
        return TF
    def getDocumentsRank(self,query):
        query = word_tokenize(query)
        TD = self.getTDmatrix(query)
        IDF = self.getIDF(query,TD)
        TF = self.getTermFrequency(query,TD)
        ranks=defaultdict(0)
        for q in query:
            for word,D in TD.keys():
                if(word==q):
                    numerator = TD[word,D]*(self.k+1)
                    denominator = TF[q]+self.k*(1-self.b+self.b*(self.D[D]/self.d_avg))
                    ranks[D]+=IDF[q]*(numerator/denominator)
        return ranks
        
            
    

