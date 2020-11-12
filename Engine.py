from ranking import BM25Ranker
from inverted_index import index,N
query = input("Enter the query:")
ranker = BM25Ranker(index,N,10,10)
documentsRank = ranker.getDocumentsRank(query)
for docID in documentsRank.keys():
    print(index.documents[docID],documentsRank[docID])

