import nltk
import os
from itertools import chain
from nltk.corpus import wordnet
from collections import defaultdict
from nltk.stem.snowball import EnglishStemmer
nltk.download('stopwords')
import pickle

class Index:
	""" Inverted index datastructure """
	def __init__(self, tokenizer, stemmer=None, stopwords=None):
		self.tokenizer = tokenizer
		self.stemmer = stemmer
		self.invertedindex = defaultdict(list)
		self.documentWords={}
		self.documents = {}
		self.noOfDocuments=0
		self.__unique_id = 0
		if not stopwords:
			self.stopwords = set()
		else:
			self.stopwords = set(stopwords)
	def add(self,file_path):
		count=0
		document = open(file_path,'r').read()
		for token in [t.lower() for t in nltk.word_tokenize(document)]:
			if token in self.stopwords:
				continue
			if self.stemmer:
				token = self.stemmer.stem(token)
			postingDocument = [postingList[0] for postingList in self.invertedindex[token]]
			if self.__unique_id not in postingDocument:
				self.invertedindex[token].append([self.__unique_id,1])
			else:
				self.invertedindex[token][postingDocument.index(self.__unique_id)][1]+=1
			count+=1
		self.documentWords[self.__unique_id]=count
		self.documents[self.__unique_id] = file_path
		self.__unique_id += 1
	def lookup(self, word):
		word = word.lower()
		if self.stemmer:
			word = self.stemmer.stem(word)
		for id,count in self.invertedindex.get(word,None):
			if(id is not None):
				return self.documents.get(id,None),count
			else:
				return None
base_path = u"C:/Users/sreedhar/Documents/Corpus"
documents = os.listdir(base_path)
N=0
indexobject = Index(nltk.word_tokenize, 
              EnglishStemmer(), 
              nltk.corpus.stopwords.words('english'))
for document in documents:
	indexobject.noOfDocuments +=1
	path = os.path.join(base_path,document)
	indexobject.add(path)
#print(indexobject.invertedindex)
#print(indexobject.documentWords)
pickle_out = open("index.pkl", 'wb') 
pickle.dump(indexobject, pickle_out)
pickle_out.close()
