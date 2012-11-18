#!/usr/bin/env python

import time
import utils
import operator
import tfidf

#centroid
#{tag:'tagName', tokens:{word1:tf-idfValue, word2:tf-idfValue...}}


class PNAClassifier(object):
	def __init__(self,centroids):
		self.centroids = centroids
		self.tfidf = tfidf.TfIdf();
		pass
		
	def runPNAClassifier(self, outerLimit, innerLimit, k):
		tagDistances = []
		self.tfidf.add_input_document("the cat in the hat")
		self.tfidf.save_corpus_to_file('tfidf.txt','stopwords.txt')
		return 0
		
def main():
	centroids = [{}]
	classifier = PNAClassifier(centroids)
	classifier.runPNAClassifier(10,5,100)
	return 0
if __name__=="__main__":
    main()
