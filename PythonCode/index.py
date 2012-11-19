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
from nltk.corpus import stopwords


def tokenize(text):
    #tokens = re.findall("[\w']+", text.lower())
    tokens = text.split()
    return [porter2.stem(token) for token in tokens]

class Indexer(object):
    def __init__(self):
        self.tfidfOb = tfidf.TfIdf()
        self.tagInfo = {}

# items is the corpus
    def index(self,items):
        db = utils.connect_db('stack', remove_existing=True)

        filteredQuestion = {}

        for question in items:
            wordSet = set()
            filtered_words = [w for w in tokenize(question["body"]) if not w in stopwords.words('english')]
            paragraph = ""
            for myword in filtered_words:
                paragraph += myword + " "
            filteredQuestion[question["question_id"]] = paragraph
            self.tfidfOb.add_input_document(paragraph)

#        for token in tokens:
#            wordSet.add(token)

            for tag in question["tags"]:
                if not self.tagInfo.has_key(tag):
                    self.tagInfo[tag] = {}
                    self.tagInfo[tag]["tokens"] = {}
                    self.tagInfo[tag]["count"] = 0
                self.tagInfo[tag]["count"] += 1

        for question in items:   # may need to watch out for reused generators!!!
            for tag in question["tags"]:
                tfidfDict = self.tfidfOb.get_doc_keywords_dict(filteredQuestion[question["question_id"]])
                for term in tfidfDict:
                    if not self.tagInfo[tag]["tokens"].has_key(term):
                        self.tagInfo[tag]["tokens"][term] = 0
                    self.tagInfo[tag]["tokens"][term] += tfidfDict[term]

        for tag in self.tagInfo:
            for term in self.tagInfo[tag]["tokens"]:
                newAvg = float(self.tagInfo[tag]["tokens"][term])/float(self.tagInfo[tag]["count"])
                self.tagInfo[tag]["tokens"][term] = newAvg
        
        tagInfoStructure = []
        for tag in self.tagInfo:
            tagInfoStructure.append({'tag':tag,'tokens':self.tagInfo[tag]['tokens']})
        self.tagInfo = tagInfoStructure
        


        self.tfidfOb.save_corpus_to_file("tfidfValues.txt","stopwords.txt")
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
