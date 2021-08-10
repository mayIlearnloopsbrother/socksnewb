#!/usr/bin/python3

import socket               #importing the socket module

a = input("enter full website name.. e.g. www.abc.com: ")     # stores user input in the variable a

print(socket.gethostbyname(str(a)))     # printing the variable 'a' to turn it into an ip address by using the 'socket.gethostbyname' class
