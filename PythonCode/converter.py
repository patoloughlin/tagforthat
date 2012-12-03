#!/usr/bin/python
import fileinput
import ujson

def loadfile(line):
    yield ujson.loads(line)

def main():
    allquestions = []
    ids = set()
    count = 0
    for line in fileinput.input():
        somequestions = loadfile(line)
        for item in somequestions:
            for question in item['questions']:
                currentdict = {}
                tempid = question['question_id']
                print tempid

                if tempid in ids:
                    print "error..."

                # behold...the if-statement of doom!
                if (tempid not in ids and
                    question.has_key('tags') and
                    question.has_key('up_vote_count') and
                    question.has_key('down_vote_count') and
                    question.has_key('view_count') and
                    question.has_key('score') and
                    question.has_key('body') and
                    question.has_key('title')):
                        currentdict['question_id'] = tempid
                        currentdict['tags'] = question['tags']
                        currentdict['up_vote_count'] = question['up_vote_count']
                        currentdict['down_vote_count'] = question['down_vote_count']
                        currentdict['view_count'] = question['view_count']
                        currentdict['score'] = question['score']
                        currentdict['title'] = question['title']
                        currentdict['body'] = question['body']
                        count += 1
                        ids.add(tempid)
                        allquestions.append(currentdict)

        del somequestions
        del currentdict

    with open("allquestions.json", "a") as myfile:
        for element in allquestions:
            myfile.write(ujson.dumps(element))
            myfile.write("\n")


if __name__=="__main__":
    main()

