import nltk
import os
from itertools import chain
from nltk.corpus import wordnet
from collections import defaultdict
from nltk.stem.snowball import EnglishStemmer
nltk.download('stopwords')

class Index:
	""" Inverted index datastructure """
	def __init__(self, tokenizer, stemmer=None, stopwords=None):
		self.tokenizer = tokenizer
		self.stemmer = stemmer
		self.index = defaultdict(list)
		self.documents = {}
		self.__unique_id = 0
		if not stopwords:
			self.stopwords = set()
		else:
			self.stopwords = set(stopwords)
	def add(self,file_path):
		document = open(file_path,'r').read()
		for token in [t.lower() for t in nltk.word_tokenize(document)]:
			if token in self.stopwords:
				continue
			if self.stemmer:
				token = self.stemmer.stem(token)
			postingDocument = [postingList[0] for postingList in self.index[token]]
			if self.__unique_id not in postingDocument:
				self.index[token].append([self.__unique_id,1])
			else:
				self.index[token][postingDocument.index(self.__unique_id)][1]+=1
		self.documents[self.__unique_id] = file_path
		self.__unique_id += 1
	def lookup(self, word):
		word = word.lower()
		if self.stemmer:
			word = self.stemmer.stem(word)
		for id,count in self.index.get(word,None):
			if(id is not None):
				return self.documents.get(id,None),count
			else:
				return None
base_path = "/home/midhilesh/Documents/sem 9/IR/Corpus"
documents = os.listdir(base_path)
index = Index(nltk.word_tokenize, 
              EnglishStemmer(), 
              nltk.corpus.stopwords.words('english'))
for document in documents:
	path = os.path.join(base_path,document)
	index.add(path)
       
