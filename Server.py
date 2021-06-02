import socketserver
import struct

from typing import Tuple

from Settings import *

TCP_LENGTH = 4

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        while True:
            dataLengthStr = self.request.recv(4)
            dataLength = sum(list(bytes(dataLengthStr)))
            self.data = self.request.recv(dataLength).decode('UTF-8', 'ignore').strip()
            if not self.data:
                break
            print(TCPHandler.get_ligand_target(self.data))
            self.feedback_data = "Return message".encode('utf-8')
            self.request.sendall(self.feedback_data)

    @staticmethod
    def get_ligand_target(pattern: str) -> Tuple[str, str, str]:
        uid, ligandSmiles, targetFASTA = pattern.split('&')

        return uid, ligandSmiles, targetFASTA


if __name__ == '__main__':
    host = LOCALHOST
    port = PORT
    server = socketserver.ThreadingTCPServer((host, port), TCPHandler)
    server.serve_forever()
    server.server_close()
