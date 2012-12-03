import socket
import sys
import classifier
import test_corpus
import index
import utils

from pymongo import DESCENDING

#Setting up corpus 

db = utils.connect_db('stack',remove_existing=False)
myIndexer = index.Indexer(db)

tags_ = myIndexer.centroids.find()
tags = tags_.sort('tag',DESCENDING)
finalList = [doc for doc in tags]

q_ = myIndexer.questions.find()
questions = q_.sort('question_id',DESCENDING)
finalQuestions = [doc for doc in questions]
classy = classifier.PNAClassifier(finalList,finalQuestions)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8080)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print sys.stderr, 'connection from', client_address
        size = connection.recv(16)
        print sys.stderr, 'Recieving "%s" bytes' % size
        connection.sendall('send data')
        data = connection.recv(int(size))
        print >> sys.stderr, 'Recieved "%s"' % data
        responce = classy.runPNAClassifier(10,10, data)
	response = 'Server Response'
	connection.sendall(str(len(str(responce))))
	connection.recv(16)
	connection.sendall(str(responce))
            
            
    finally:
        # Clean up the connection
        connection.close()