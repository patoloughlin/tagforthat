#!/usr/bin/python

import index
import classifier
import test_corpus
import sys
import utils
import ujson

def loadAllQuestions():
    f = open('../finalData/allquestions.json', 'r')
    for line in f:
        yield ujson.loads(line)

if __name__=="__main__":
    items = loadAllQuestions()
    totalQuestions = []

    for thing in items:
        totalQuestions.append(thing)

    db = utils.connect_db('stack')
    myIndexer = index.Indexer(db)
    classy = classifier.PNAClassifier(myIndexer.tagInfo,totalQuestions)
    recommended_tags = classy.runPNAClassifier(4,3, sys.argv[1])
    print recommended_tags

