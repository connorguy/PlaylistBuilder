import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((socket.gethostname(), 6969))
msg = open('client_info.json').read()
#msg = "magnuscaligo 32.6 -116.9 Highway to hell"
msg = "34 -118.2"
typeMsg = 2
print msg

size = len(msg)

ba = bytearray(4)
value = struct.pack("I", size)


sock.send(chr(typeMsg))
sock.send(value)
sock.send(msg)

