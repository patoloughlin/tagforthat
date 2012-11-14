#!/usr/bin/env python

import time
import utils
import operator

"""
def process_tweets(method,label):
    print 'starting %s'%label
    tweets = utils.read_tweets()
    start_time = time.time()
    method(tweets)
    end_time = time.time()
    print 'done with %s after %.3f seconds'%(label,end_time-start_time)
"""

def main():
    db = utils.connect_db('stack', remove_existing=True)

    items = utils.read_items()

    counter = {}
    numtags = 0
    numquestions = 0

    for item in items:
        for question in item["questions"]:
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
    main()
