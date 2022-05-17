import requests
import time
import colorama
from colorama import *
import os

os.system("cls || clear")

rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000')
with open('proxies.txt', 'wb') as fp:
    fp.write(rsp.content)
    print(Fore.CYAN + "Proxies Nuevos Obtenidos")
