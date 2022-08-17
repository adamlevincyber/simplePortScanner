#!/bin/python

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid number of arguments!")
    print("Syntax: python3 simplePortScanner.py <ip>")

print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        #print("Checking port {}" .format(port))
        
        if result == 0:
            print("Port {} is open" .format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program gracefully.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()