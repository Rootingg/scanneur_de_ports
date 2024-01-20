import socket
import threading
import sys
from datetime import datetime
import subprocess

remoteIP = input("Entrer l'ip à scanner : ")

print("-"*60)
print("Lancement du scan des ports de la machine "+remoteIP)
print("-"*60)
t1 = datetime.now()

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteIP, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
            print(f"Port {port} : Ouvert ({service})")
        except:
            print(f"Port {port} : Ouvert")
    sock.close()

try:
    for port in range(1,10000):
        threading.Thread(target=scan_port, args=(port,)).start()

except KeyboardInterrupt:
    print("Vous avez appuyé sur Ctrl+C.")
    sys.exit()

except socket.error:
    print("Impossible de se connecter au serveur.")
    sys.exit()

t2 = datetime.now()
total = t2-t1

print(f"Scan complété en : {total}")