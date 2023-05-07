#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8081
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        header = "HTTP/1.1 200 OK\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
    except IOError:
        
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1><center> 404 Not Found </center></h1></body></html>\r\n".encode())

    connectionSocket.close()
serverSocket.close()
sys.exit()