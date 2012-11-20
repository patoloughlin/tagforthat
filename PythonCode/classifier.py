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
    def __init__(self,centroids,corpus):
        self.centroids = centroids
        self.corpus = corpus
        self.tfidf = tfidf.TfIdf('tfidfValues.txt')
        pass
    def runPNAClassifier(self, outerLimit, innerLimit, query):
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
        loadedQuestions = []
        questionDistances = {}
        for tag in topTags:
            for question in self.corpus:
				if tag in question['tags']:
					questionDict = {}
					questionDict['tokens'] = self.tfidf.get_doc_keywords_dict(question['body'])
					questionDict['tags'] = question['tags']
					loadedQuestions.append(questionDict)
        for question in loadedQuestions:
            distance = calculateDistance(question,queryDict)
            for tag in question['tags']:
                if tag in topTags:
                    if tag in questionDistances:
                        questionDistances[tag]['distance'] += distance
                        questionDistances[tag]['count'] += 1
                    else:
                        questionDistances[tag] = {}
                        questionDistances[tag]['distance'] = distance
                        questionDistances[tag]['tag'] = tag
                        questionDistances[tag]['count'] = 1
        for tag in questionDistances:
            questionDistances[tag]['distance'] = (questionDistances[tag]['distance'] * 1.0) / (questionDistances[tag]['count'] * 1.0)
        topTags = sorted(questionDistances, key= lambda X : questionDistances[X]['distance'])[:innerLimit]
        print topTags
        return topTags
    
def main():
	centroids = [{'tag':'c#','tokens':{'c#':1.3862943611198906}},{'tag':'java','tokens':{'java':.2}}]
	classifier = PNAClassifier(centroids)
	classifier.runPNAClassifier(4,2,"linux is broken")
	return 0
if __name__=="__main__":
    main()
