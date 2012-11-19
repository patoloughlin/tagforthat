
There's a Tag for That!
Readme
---------

CLONING
-------
First you must clone the git repository:

$ git clone https://github.com/patoloughlin/tagforthat.git

If, for whatever reason the clone command is having a difficult time, you 
may manually go to the web page and download the .git repository as a zip file.

EXPANDING THE GIT REPO
-------
$ git checkout master
$ git reset HEAD --hard

TESTING THE PROGRAM
------

Mongo is required to run this program!
# mongod

The program may either be tested by use of a small script with your custom queries, 
or by running the unit tests.

To run the sample script:
$ python sampleRun.py "this is my test query. Pointers are confusing to my noobie self"
This will return a list of recommended tags for your query.

PLEASE NOTE that this is running off of our (rather small) test corpus. If your query gets 
an odd recommendation, it's probably because our corpus isn't large enough. The suggested 
query topics for test purposes include "Windows", "Linux", "pointers", and "cats", if the 
latter is used conseratively.

To run the unit test:
$ python test_corpus.py

-------


The tiny corpus may be found in test_corpus.py. Enjoy!

