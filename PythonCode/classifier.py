#!/usr/bin/env python

import time
import utils
import operator
import tfidf
import test_corpus

#centroid
#{tag:'tagName', tokens:{word1:tf-idfValue, word2:tf-idfValue...}}


class PNAClassifier(object):
	def __init__(self,centroids):
		self.centroids = centroids
		self.tfidf = tfidf.TfIdf('tfidfValues.txt')
		pass
		
	def runPNAClassifier(self, outerLimit, innerLimit, k, query):
		tagDistances = [{}]
		#Calculate tf-idf vector of query based off of idf vector in database
		
		#for centroid in self.centroids:
			#Calculate distance of query to centroid
			#Save distance into tagDistance array
		
		#for question in test_corpus.corpus:
		#	self.tfidf.add_input_document(question["body"])
		#self.tfidf.save_corpus_to_file("termFrequency.txt","stopwords.txt")
		print self.tfidf.get_doc_keywords_dict(query)
		return 0
		
def main():
	centroids = [{}]
	classifier = PNAClassifier(centroids)
	classifier.runPNAClassifier(10,5,100,"c# is king")
	return 0
if __name__=="__main__":
    main()
