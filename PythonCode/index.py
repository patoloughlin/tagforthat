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

"""
def checkpoint1(items):
    for question in items:
        numquestions += 1
        for tag in question["tags"]:
            if not counter.has_key(tag):
                counter[tag] = 0
            counter[tag] += 1
            numtags += 1

    tagfreqList = sorted(counter.iteritems(), key=operator.itemgetter(1),reverse=True)

    for tag in tagfreqList[:500]:
#        print str(tag)
        with open("tags.txt", "a") as myfile:
            myfile.write(tag[0] + "\n")
        with open("nums.txt", "a") as mynumsfile:
            mynumsfile.write(str(tag[1]) + "\n")

    print "total unique tags:" + str(len(tagfreqList))
    print "total number of tags:" + str(numtags)
    print "total number of questions:" + str(numquestions)
    print "average tags per question:" + str(float(numtags)/float(numquestions))


def tokenize(text):
    tokens = re.findall("[\w']+", text.lower())
    return [porter2.stem(token) for token in tokens]
"""
class Indexer(object):
    def __init__(self):
        self.tfidfOb = tfidf.TfIdf()
        selftagInfo = {}

# items is the corpus
    def index(items):
        db = utils.connect_db('stack', remove_existing=True)

        for question in items:
            wordSet = set()
            tfidfOb.add_input_document(question["body"])

#        for token in tokens:
#            wordSet.add(token)

            for tag in question["tags"]:
                if not tagInfo.has_key(tag):
                    tagInfo[tag] = {}
                    tagInfo[tag]["tokens"] = {}
                    tagInfo[tag]["count"] = 0
                tagInfo[tag]["count"] += 1

        for question in items:   # may need to watch out for reused generators!!!
            for tag in question["tags"]:
                tfidfDict = tfidfOb.get_doc_keywords_dict(question["body"])
                for term in tfidfDict:
                    if not tagInfo[tag]["tokens"].has_key(term):
                        tagInfo[tag]["tokens"][term] = 0
                    tagInfo[tag]["tokens"][term] += tfidfDict[term]

        for tag in tagInfo:
            for term in tagInfo[tag]["tokens"]:
                newAvg = float(tagInfo[tag]["tokens"][term])/float(tagInfo[tag]["count"])
                tagInfo[tag]["tokens"][term] = newAvg

        for item in tagInfo:
            print "tag: " + str(item)
            for thing in tagInfo[item]:
                print thing
                print tagInfo[item][thing]
                print "   ====    "
            print "--------"

        tfidfOb.save_corpus_to_file("tfidfValues.txt","stopwords.txt")
#    counter_real = Counter(biglist)
        #print counter_real
#    for token in wordSet:
#        print tfidfOb.get_doc_keywords_dict(token)

#    X = {tag = "c++", tokens={"i":3,"am":4} }

"""
if __name__=="__main__":
    items = utils.read_items()
    index(items)
"""
