import sys,os,re,socket,binascii,time,json,random,threading,pprint,smtplib,telnetlib,os.path,hashlib,string,glob,sqlite3,argparse,marshal,base64,colorama,requests
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing.dummy import Pool
from platform import system
from time import strftime
from colorama import Fore,init, Style
os.system("title Mass IP Form Domain List Coded By Bisno Das")
def screen_clear():
    _ = os.system('cls')
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE
meg = Fore.MAGENTA

screen_clear()
print("""
     ███▄ ▄███▓ ▄▄▄        ██████   ██████     ██▓ ██▓███     ▓█████▄  ▒█████   ███▄ ▄███▓ ▄▄▄       ██▓ ███▄    █ 
    ▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▒██    ▒    ▓██▒▓██░  ██▒   ▒██▀ ██▌▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▓██▒ ██ ▀█   █ 
    ▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄      ▒██▒▓██░ ██▓▒   ░██   █▌▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ▒██▒▓██  ▀█ ██▒
    ▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒   ░██░▒██▄█▓▒ ▒   ░▓█▄   ▌▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ░██░▓██▒  ▐▌██▒
    ▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██████▒▒   ░██░▒██▒ ░  ░   ░▒████▓ ░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒░██░▒██░   ▓██░
    ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░   ░▓  ▒▓▒░ ░  ░    ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░   ▒ ▒ 
    ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░    ▒ ░░▒ ░         ░ ▒  ▒   ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░░   ░ ▒░
    ░      ░     ░   ▒   ░  ░  ░  ░  ░  ░      ▒ ░░░           ░ ░  ░ ░ ░ ░ ▒  ░      ░     ░   ▒    ▒ ░   ░   ░ ░ 
           ░         ░  ░      ░        ░      ░                 ░        ░ ░         ░         ░  ░ ░           ░ 
                                                               ░                                                   
""")

def getIP(site):
		try:
			if 'http://' not in site:
				IP1 = socket.gethostbyname(site)
				print (f"{meg} IP ==> "+IP1)
				open('ip.txt', 'a').write(IP1+'\n')
			elif 'http://' in site:
				url = site.replace('http://', '').replace('https://', '').replace('/', '')
				IP2 = socket.gethostbyname(url)
				print (f"{meg} IP ==> "+IP2)
				open('ip.txt', 'a').write(IP2+'\n')
	
		except:
			pass


		
nam = input(Fore.GREEN+f" Enter Your iPS Lists  ==> ")
ooo = open(nam,'r').read().splitlines()
worker = int(input(Fore.MAGENTA+f" Enter Your Thread Number ==> "))
ThreadPool = Pool(worker)
Threads = ThreadPool.map(getIP, ooo)


with open(nam) as f:
    for i in f:
        getIP(i)
		
