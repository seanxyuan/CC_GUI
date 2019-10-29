import bluetooth

import gzip
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO



# setup server
port = 1
target_addr = '98:D3:31:FB:15:14'
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_addr, port))

x = sock.recv(9600)
buf = StringIO(x)
f = gzip.GzipFile(fileobj=buf)
f.read()
