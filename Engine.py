from ranking import BM25Ranker
import pickle
from inverted_index import Index
pickle_in = open("index.pkl","rb")
indexobj= pickle.load(pickle_in)
query = input("Enter the query:")
ranker = BM25Ranker(indexobj,indexobj.noOfDocuments,1.5,0.75)
documentsRank = ranker.getDocumentsRank(query)
for docID in documentsRank.keys():
	if(documentsRank[docID]>0.5):
    		print(indexobj.documents[docID],documentsRank[docID])

