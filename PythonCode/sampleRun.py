#!/usr/bin/python

import index
import classifier
import test_corpus
import sys

if __name__=="__main__":
    items = test_corpus.corpus
    myIndexer = index.Indexer()
    myIndexer.index(items)
    classy = classifier.PNAClassifier(myIndexer.tagInfo,items)
    recommended_tags = classy.runPNAClassifier(4,3, sys.argv[1])
    print recommended_tags

