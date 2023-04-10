
import sys
import socket
from datetime import datetime



target = input(str("Target IP address: "))

print("_" * 50)
print("Scanning Target: " + target)
print("_" * 50)

try:

    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()

except socket.error:
    print("Oops")
    sys.exit()