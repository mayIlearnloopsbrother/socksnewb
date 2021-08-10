#!/usr/bin/python3

import socket

a = input("enter full website name.. e.g. www.abc.com: ")

print(socket.gethostbyname(str(a))) 
