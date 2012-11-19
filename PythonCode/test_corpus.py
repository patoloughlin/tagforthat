#!/usr/bin/env python

import unittest
import sys,os
import index
import classifier

path = os.path.abspath(__file__)
sys.path.append(os.path.join(os.path.dirname(path), "../"))

import utils
from settings import settings


corpus = [
    dict(question_id=0,tags=["Windows","crash","bluescreen"],body="Help! Windows 8 crashed on me. I unplugged my ethernet cable and it gave me a blue screen!"),
    dict(question_id=1,tags=["Windows","C#","Visual Studio"],body="Hey there, I am trying to write a C# program in Visual Studio for my university. I am confused, please help."),
    dict(question_id=2,tags=["Linux","crash","drivers"],body="Hi, I recently updated the Linux kernel to 3.03 and my ATI drivers as well. When using modprobe I got a kernel panic! :("),
    dict(question_id=3,tags=["C++","pointer","graphics"],body="In CSCE 441, I heard we have to use quite a few pointers to complete our graphics homework. The program needs to be fast."),
    dict(question_id=4,tags=["Java","Android","NullPointer"],body="I'm writing an Android java application, and I can't seem to get around this NullPointerException. I thought java didn't have pointers"),
    dict(question_id=5,tags=["C++","pointer","dereference"],body="C++ noobie here. How, exactly do pointers and dereferencing work? It seems like a whole lot of guesswork to me."),
    dict(question_id=6,tags=["C#","Windows","Mono"],body="Hi fellow Windows fanatics! Maybe we should use Monodevelop for our prefered language to allow for cross-platform coding."),
    dict(question_id=7,tags=["Linux","Slackware","package"],body="Hello everybody. Recently, I borked my slackware install (corrupt kernel) by using third-party packages managers like slapt-get. Please teach me to be a responsible slacker!"),
    dict(question_id=8,tags=["Java","graphics","meshes"],body="Hey there, I've been trying to create an algorithm that will programmatically create meshes using Java and lwjgl. I need help on this."),
    dict(question_id=9,tags=["crash","Windows","cats"],body="Help! My cat walked across the keyboard and i used windows on my windows pc and my computer crashed!! help!"),
    dict(question_id=10,tags=["Linux","crash","C#"],body="please help me use C# on Linux. Support for a non-windows platform seems very limited."),
]

class TestCoreAlg(unittest.TestCase):
    def setUp(self):
		self.index = index.Indexer()
		self.index.index(corpus)
		self.classifier = classifier.PNAClassifier(self.index.tagInfo,corpus)
		print "this is the setup method"

    def test_calculate_tfidf(self):
		self.classifier.runPNAClassifier(4,2,"my cat broke my windows pc")
		self.assertEqual(1,0)

    # Add more tests here.

if __name__ == '__main__':
    unittest.main()

