#!/usr/bin/env python

import time
import utils
import operator
import tfidf
import test_corpus
import math

#centroid
#{tag:'tagName', tokens:{word1:tf-idfValue, word2:tf-idfValue...}}

def calculateDistance(X, Y):
    rvalue = 0
    for token in Y['tokens']:
        if token in X['tokens']:
            rvalue += (Y['tokens'][token] - X['tokens'][token]) * (Y['tokens'][token] - X['tokens'][token])
        else:
            rvalue += Y['tokens'][token] * Y['tokens'][token]
    for token in X['tokens']:
        if token not in Y['tokens']:
            rvalue += X['tokens'][token] * X['tokens'][token]
    rvalue = math.sqrt(rvalue)
    return rvalue


class PNAClassifier(object):
	def __init__(self,centroids):
		self.centroids = centroids
		self.tfidf = tfidf.TfIdf('tfidfValues.txt')
		pass
		
	def runPNAClassifier(self, outerLimit, innerLimit, k, query):
		tagDistances = {}
		topTags = []
		#Calculate tf-idf vector of query based off of idf vector in database
		queryDict = {}
		queryDict['tokens'] = self.tfidf.get_doc_keywords_dict(query)
		for centroid in self.centroids:
			#Calculate distance of query to centroid
			#Save distance into tagDistance array
			tagDistances[centroid['tag']] = {'tag':centroid['tag'],'distance':calculateDistance(centroid,queryDict)}
		topTags = sorted(tagDistances, key= lambda X : tagDistances[X]['distance'])[:outerLimit]
		print topTags
		#Loop throught the top tags(outerLimit is the cut off for this)
		#We will now get the knn neighbors of all the questions inside of the outerLimit
		#for tag in topTags:
			
		print queryDict['tokens']
		return 0
		
def main():
	centroids = [{'tag':'c#','tokens':{'c#':1.3862943611198906}},{'tag':'java','tokens':{'java':.2}}]
	classifier = PNAClassifier(centroids)
	classifier.runPNAClassifier(2,1,5,"linux is broken")
	return 0
if __name__=="__main__":
    main()
