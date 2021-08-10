# socksnewb

#!/usr/bin/python3

import socket                                               ---> importing the socket class

a = input("enter full website name.. e.g. www.abc.com: ")   ---> setting user input to the variable 'a' 

print(socket.gethostbyname(str(a)))                         ---> printing the user input 'str(a)' into ip address by the use of 'socket.gethostbyname'
