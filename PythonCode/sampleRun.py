#!/usr/bin/python

import index
import classifier
import test_corpus
import sys
import utils
import ujson
from pymongo import ASCENDING, DESCENDING

def loadAllQuestions():
    f = open('../finalData/allquestions.json', 'r')
    for line in f:
        yield ujson.loads(line)

if __name__=="__main__":
    #items = loadAllQuestions()
    #totalQuestions = []

    #for thing in items:
    #    totalQuestions.append(thing)

    db = utils.connect_db('stack',remove_existing=False)
    myIndexer = index.Indexer(db)

    tags_ = myIndexer.centroids.find()
    tags = tags_.sort('tag',DESCENDING)
    finalList = [doc for doc in tags]

    q_ = myIndexer.questions.find()
    questions = q_.sort('question_id',DESCENDING)
    finalQuestions = [doc for doc in questions]

    classy = classifier.PNAClassifier(finalList,finalQuestions)
    recommended_tags = classy.runPNAClassifier(4,3, sys.argv[1])
    print recommended_tags

