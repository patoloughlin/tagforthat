import socket
import sys
import classifier
import test_corpus
import index

#Setting up corpus 
items = test_corpus.corpus
myIndexer = index.Indexer()
myIndexer.index(items)
classy = classifier.PNAClassifier(myIndexer.tagInfo,items)

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
        responce = classy.runPNAClassifier(10,5, data)
	response = 'Server Response'
	connection.sendall(str(len(str(responce))))
	connection.recv(16)
	connection.sendall(str(responce))
            
            
    finally:
        # Clean up the connection
        connection.close()