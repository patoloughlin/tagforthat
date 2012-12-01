#!/usr/bin/env python

import time
import utils
import operator
import re
from stemming import porter2
from pymongo import ASCENDING, DESCENDING
from math import log
from collections import Counter
import tfidf
import itertools

"""
def tokenize(text):
    tokens = re.findall("[\w']+", text.lower())
    return [porter2.stem(token) for token in tokens]
"""

class Indexer(object):
    def __init__(self, db):
        self.tfidfOb = tfidf.TfIdf()
        self.tagInfo = {}
        self.centroids = db['centroids']
        self.mongo = db

# items is the corpus
    def index(self,items):
        
        iterators = itertools.tee(items)

        for question in iterators[0]:
            wordSet = set()
            self.tfidfOb.add_input_document(question["body"])

#        for token in tokens:
#            wordSet.add(token)

            for tag in question["tags"]:
                if not self.tagInfo.has_key(tag):
                    self.tagInfo[tag] = {}
                    self.tagInfo[tag]["tokens"] = {}
                    self.tagInfo[tag]["count"] = 0
                self.tagInfo[tag]["count"] += 1

        for question in iterators[1]:   # may need to watch out for reused generators!!!
            for tag in question["tags"]:
                #print "tag: " + str(tag)
                tfidfDict = self.tfidfOb.get_doc_keywords_dict(question["body"])
                #print tfidfDict
                for term in tfidfDict:
                    #print "YO: " + str(term)
                    if not self.tagInfo[tag]["tokens"].has_key(term):
                        self.tagInfo[tag]["tokens"][term] = 0
                    self.tagInfo[tag]["tokens"][term] += tfidfDict[term]

        for tag in self.tagInfo:
            for term in self.tagInfo[tag]["tokens"]:
                #print "tag: " + str(tag) + "\t term: " + str(term)
                newAvg = float(self.tagInfo[tag]["tokens"][term])/float(self.tagInfo[tag]["count"])
                self.tagInfo[tag]["tokens"][term] = newAvg
        
        #tagInfoStructure = []
        for tag in self.tagInfo:
            #print str(tag) + "\t" + str(self.tagInfo[tag]['tokens'])
            self.centroids.insert({'tag':tag,'tokens':self.tagInfo[tag]['tokens']})

        self.centroids.create_index([('tag',ASCENDING)])
        #self.tagInfo = tagInfoStructure
        


        self.tfidfOb.save_corpus_to_file("tfidfValues.txt","stopwords.txt")
#    counter_real = Counter(biglist)
        #print counter_real
#    for token in wordSet:
#        print tfidfOb.get_doc_keywords_dict(token)

#    X = {tag = "c++", tokens={"i":3,"am":4} }


if __name__=="__main__":
    start_time = time.time()
    items = utils.read_items()
    mydb = utils.connect_db('stack', remove_existing=True)
    indexMe = Indexer(mydb)
    indexMe.index(items)
    end_time = time.time()
    print 'done with indexing after %.3f seconds'%(end_time-start_time)
    
