import socket

from Settings import *

server = socket.socket()
host = socket.gethostname()

server.bind((host, PORT))

server.listen(5)
while True:
    c, addr = server.accept()
    c.send('Hello, world'.encode())
    c.close()
