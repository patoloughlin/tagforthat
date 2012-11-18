#!/usr/bin/env python

import time
import utils
import operator
import re
from stemming import porter2
from pymongo import ASCENDING, DESCENDING
from math import log


def tokenize(text):
    tokens = re.findall("[\w']+", text.lower())
    return [porter2.stem(token) for token in tokens]

# items is the corpus
def index(items):
    db = utils.connect_db('stack', remove_existing=True)
    

    counter = {}
    numtags = 0
    numquestions = 0

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

if __name__=="__main__":
    items = utils.read_items()
    index(items)

