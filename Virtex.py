#coding=utf-8
from zipfile import ZipFile as zip
from sys import version , platform , argv
from webbrowser import open_new_tab
from time import sleep
from os import system as sys , environ as env , W_OK as ok , stat , access , uname
from os.path import basename , isfile , realpath , exists , dirname
from urllib.request import urlopen
from urllib.error import URLError as koneksi
from socket import gethostname
from getpass import getpass
from datetime import datetime
from random import choice

warna = lambda : choice(["\033[0m","\033[90m","\033[91m","\033[92m","\033[93m","\033[94m","\033[95m","\033[96m","\033[97m"])

UPDATE = "14-03-2021 12:35"
logo = f"\033[91m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n\033[94m╔═════════════════════════════════════╗\n║\033[94m[\033[93m•\033[94m] \033[96mAuthor : \033[92m\033[4mMR-X JUNIOR\033[0m             \033[94m║\n║\033[94m[\033[93m•\033[94m] \033[96mGitHub : \033[97mgithub.com/MR-X-Junior  \033[94m║\n║\033[94m[\033[93m•\033[94m] \033[96mWA.    : \033[93m+62 85754629509        \033[94m ║\n║\033[94m[\033[93m•\033[94m] \033[96mUPDATE : {UPDATE}      \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mPython : {warna()}{version[0:6]}                \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mOS     : {warna()}{platform}                 \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mHost   : {warna()}{gethostname()}             \033[94m  ║\n║\033[94m[\033[93m•\033[94m] \033[96mTeam.  : {warna()}TNT {warna()}ANONYMOUS \033[91mINDO\033[97mNESIA\033[94m ║\n\033[94m╚═════════════════════════════════════╝"
virtex="""\033[1;94m[\033[1;91m01\033[1;94m] \033[1;91m☕⇣፟፝P፟፝A፟፝፞N̩፟፝T፟፝፞A፟፝N፟፞፝G፟፝ ፟፝M፟፞፟፝U፟፞፝N፟፝D፟፝U፟፝R፟፝ 7̩፟፝6̩፟፝9 A፟፝N፟፞፝T፟፝I A፟፝P፟፞፝E፟፝S፟፝-1-1 \n\033[1;94m[\033[1;91m02\033[1;94m] \033[1;92m☞IPHONE KILLER☜ \n\033[1;94m[\033[1;91m03\033[1;94m] \033[1;93m☬.∆.G.I.N.☬.-1 \n\033[1;94m[\033[1;91m04\033[1;94m] \033[1;94m♞™CAVALO卐DE♞TROIA♞-1-1-2-1-1 \n\033[1;94m[\033[1;91m05\033[1;94m] \033[1;95m14N Virus \n\033[1;94m[\033[1;91m06\033[1;94m] \033[1;96mĐ.Δ.Μ.Ň.į.Ҝ.Δ.ᇸ-WPS Office\n\033[1;94m[\033[1;91m07\033[1;94m] \033[1;97mdamnika\n\033[1;94m[\033[1;91m08\033[1;94m] \033[1;91mDིྀuིྀeིྀtིྀmིྀaིྀuིྀtིྀ45\n\033[1;94m[\033[1;91m09\033[1;94m] \033[1;92mfunambol\n\033[1;94m[\033[1;91m10\033[1;94m] \033[1;93mGHOSTNAME VIRTEXT GANAS\n\033[1;94m[\033[1;91m11\033[1;94m] \033[1;94mGHOSTNAME VIRTEXT PART 2\n\033[1;94m[\033[1;91m12\033[1;94m] \033[1;95m🆔❗༺🔱🔱🔱♛R̸͟͞O̸͟͞K̸͟͞E̸͟͞T̸͟͞♛G̸͟͞H̸͟͞O̸͟͞S̸͟͞T̸͟͞♛🌀1⃣9⃣4 (1)\n\033[1;94m[\033[1;91m13\033[1;94m] \033[1;96mMR.KACANG\n\033[1;94m[\033[1;91m14\033[1;94m] \033[1;97mPantang\n\033[1;94m[\033[1;91m15\033[1;94m] \033[1;91mPilus\n\033[1;94m[\033[1;91m16\033[1;94m] \033[1;92mRayhan feat agus\n\033[1;94m[\033[1;91m17\033[1;94m] \033[1;93mrv\n\033[1;94m[\033[1;91m18\033[1;94m] \033[1;94mSerigala Hitam\n\033[1;94m[\033[1;91m19\033[1;94m] \033[1;95mVIP CODE LAG BY GHOSTNAME\n\033[1;94m[\033[1;91m20\033[1;94m] \033[1;96mVIRTEKS ALI BUKAN KALENG2\n\033[1;94m[\033[1;91m21\033[1;94m] \033[1;97mVirtex by habib [VG Cyber]\n\033[1;94m[\033[1;91m22\033[1;94m] \033[1;91mVirtex lol\n\033[1;94m[\033[1;91m23\033[1;94m] \033[1;92mV̤̈Ï̤R̤̈T̤̈Ë̤Ẍ̤T̤̈ B̤̈Ÿ̤ G̤̈Ḧ̤Ö̤S̤̈T̤̈N̤̈Ä̤M̤̈Ë̤ P̤̈Ä̤R̤̈T̤̈ 2\n\033[1;94m[\033[1;91m24\033[1;94m] \033[1;93mV̺͆I̺͆R̺͆T̺͆E̺͆X̺͆T̺͆ B̺͆Y̺͆ G̺͆H̺͆O̺͆S̺͆T̺͆N̺͆A̺͆M̺͆E̺͆\n\033[1;94m[\033[1;91m25\033[1;94m] \033[1;94mVIRTEXT DAMNIKA BARU\n\033[1;94m[\033[1;91m26\033[1;94m] \033[1;95mVIRTEXT KERAD BY GHOST NAME\n\033[1;94m[\033[1;91m27\033[1;94m] \033[1;96mVIRTEXT TESTER BY GHOSTNAME\n\033[1;94m[\033[1;91m28\033[1;94m] \033[1;97mvirus 1 TU4NB4ND1T\n\033[1;94m[\033[1;91m29\033[1;94m] \033[1;91mVIRUS BY GHOSTNAME\n\033[1;94m[\033[1;91m30\033[1;94m] \033[1;92mvirus gua Mr.H4R1\n\033[1;94m[\033[1;91m31\033[1;94m] \033[1;93mVIRUS LAG BY GHOSTNAME\n\033[1;94m[\033[1;91m32\033[1;94m] \033[1;94mVIRUS LAG WA\n\033[1;94m[\033[1;91m33\033[1;94m] \033[1;95mVIRUS LORD CHOKY\n\033[1;94m[\033[1;91m34\033[1;94m] \033[1;96mVIRUS MEMATIKAN BY GHOSTNAME\n\033[1;94m[\033[1;91m35\033[1;94m] \033[1;97mVIRUS MEMATIKAN BY RIZKY GEBOY VIRTEXT\n\033[1;94m[\033[1;91m36\033[1;94m] \033[1;91mVIRUS MEMATIKAN PART 2\n\033[1;94m[\033[1;91m37\033[1;94m] \033[1;92mVIRUS MEMATIKAN PART 3\n\033[1;94m[\033[1;91m38\033[1;94m] \033[1;93mVIRUS MEMATIKAN PART 4\n\033[1;94m[\033[1;91m39\033[1;94m] \033[1;94mVIRUS MEMATIKAN PART 5\n\033[1;94m[\033[1;91m40\033[1;94m] \033[1;95mVirus Mr.f4r!5\n\033[1;94m[\033[1;91m41\033[1;94m] \033[1;96mvirus si error\n\033[1;94m[\033[1;91m42\033[1;94m] \033[1;97mVIRUS TEXT TEST GHOSTNAME\n\033[1;94m[\033[1;91m43\033[1;94m] \033[1;91mvirus-1\n\033[1;94m[\033[1;91m44\033[1;94m] \033[1;92mvirus\n\033[1;94m[\033[1;91m45\033[1;94m] \033[1;93mvirus3ME\n\033[1;94m[\033[1;91m46\033[1;94m] \033[1;94mvirus4ME\n\033[1;94m[\033[1;91m47\033[1;94m] \033[1;95mvirushari2\n\033[1;94m[\033[1;91m48\033[1;94m] \033[1;96mVirusPending+Legh\n\033[1;94m[\033[1;91m49\033[1;94m] \033[1;97mVIRUSSETANOFFICIAL\n\033[1;94m[\033[1;91m50\033[1;94m] \033[1;91mVirusWaLag\n\033[1;94m[\033[1;91m51\033[1;94m] \033[1;95m🈴🈴🔝🔝🔝☬ŘÅJÃ⚔ŤĔŘØŘ♐8⃣7⃣9⃣♐☬🔝🔝🔝🈴🈴\n\033[1;94m[\033[1;91m52\033[1;94m] \033[1;92mATTACKER ALON\n\033[1;94m[\033[1;91m53\033[1;94m] \033[1;93mFrezzN00b\n\033[1;94m[\033[1;91m54\033[1;94m] \033[1;94mHekelKokUnicodeByFrezz\n\033[1;94m[\033[1;91m55\033[1;94m] \033[1;95mKode Lag ★ISL★-1-1-1-1\n\033[1;94m[\033[1;91m56\033[1;94m] \033[1;96mNyai•Annah\n\033[1;94m[\033[1;91m57\033[1;94m] \033[1;97mSCRIPT~WHATSAPP\n\033[1;94m[\033[1;91m58\033[1;94m] \033[1;91mSerigala Hitam\n\033[1;94m[\033[1;91m59\033[1;94m] \033[1;92mVIRτΣXGΔПΔς\n\033[1;94m[\033[1;91m60\033[1;94m] \033[1;96mUNDUH SEMUA VIRTEX\n\033[1;94m[\033[1;91m99\033[1;94m] \033[1;93mKEMBALI KE MENU UTAMA\n\033[1;94m[\033[1;91m00\033[1;94m] \033[1;91mKELUAR DARI PROGRAM"""

def show(file):
	try:
		a = isfile(file)
		if a:
			b = sys(f"termux-open --view {file}")
			if b != 0:
				print (f"\033[0m{basename(argv[0])} : Terjadi Kesalahan {b} :(")
				sleep(1)
			else:
				sleep(1)
		else:
			print (f"\033[94m[\033[91m!\033[94m] \033[93mFile \033[91m{file} \033[93mNot Found")
			sleep(1)
	except FileNotFoundError:
		print (f"\033[94m[\033[91m!\033[94m] \033[4m{file} \033[93mNot Found")
		sleep(0.1)

def web(url):
	print ("\033[94m[\033[93m!\033[94m] \033[93mMembuka",url)
	a = sys(f"xdg-open {url}")
	if a != 0:
		b = open_new_tab(url)
		if b:
			sleep(0.5)
		else:
			print (f"\033[94m[\033[93m!\033[94m] \033[93mGagal Membuka {url}")
	else:
		sleep(0.5)
	
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):
    if isfile(file_path):
        file_info = stat(file_path)
        return convert_bytes(file_info.st_size)

def get(url , save):
	print ("\033[94m[\033[93m!\033[94m] \033[93mDownloading\033[96m",save)
	total = 0
	Data = []
	wibu = True
	while wibu:
		try:
			a = urlopen(url)
			print ("\033[94m[\033[93m✓\033[94m] \033[93mURL :",a.geturl())
			Data.append(a.read())
			print ("\033[94m[\033[93m✓\033[94m] \033[93mStatus :",a.status)
			with open(save,'w') as b:
				b.write(Data[0].decode('utf-8'))
				print (f"\033[94m[\033[93m✓\033[94m] \033[92mNama File : {basename(b.name)}\n\033[94m[\033[93m✓\033[94m] \033[92mSize : {file_size(b.name)}\n\033[94m[\033[93m✓\033[94m] \033[92mFile Tersimpan Di : {realpath(b.name)}")
				c = input('\033[94m[\033[93m?\033[94m] \033[97mLihat Hasil Download [\033[92mY\033[97m/\033[91mn\033[97m] \033[95m ').lower()
				if c == 'y':
					show(b.name)
					break
				else:
					break
		except koneksi as ayu:
			total += 1
			if total == 5:
				print ("\033[94m[\033[93m!\033[94m] \033[93mGagal Terhubung Ke Server\n\n\tCoba :\n\t\t• Nonaktifkan mode pesawat\n\t\t• Aktifkan data seluler atau Wi-Fi\n\t\t• Periksa sinyal di area Anda\n",ayu)
				exit()
			else:
				print ("\033[94m[\033[93m!\033[94m] \033[93mMencoba menghubungkan ulang ke server")
				sleep(1.5)

#PILIH JENIS VIRTEX 
def main():
	while True:
		sys('clear')
		print (logo)
		try:
			print ("\033[1;92mPILIH JENIS VIRTEX")
			print (43*'\033[1;96m=')
			print (virtex)
			v = int(input("\033[1;92m>>>> \033[1;96m"))
			if v == 99:
				sys('clear')
				menu()
				break
			elif v== 0:
				exit()
			elif v== 60:
				print ("\033[94m[\033[93m!\033[94m] \033[93mDownloading virtex-master.zip")
				try:
					data = urlopen("https://rahmat232.000webhostapp.com/virtex-master.zip").read()
					open('virtex-master.zip','wb').write(data)
				except koneksi:
					print ("\033[94m[\033[93m!\033[94m] \033[93mTidak Ada Koneksi")
					sleep (2.5)
					main()
				except Exception as err:
					print ("\033[94m[\033[93m!\033[94m] \033[93m",err)
					exit()
				a = "virtex-master.zip"
				if exists(a) and isfile(a):
					b = dirname(realpath(a))
					c = access(b,ok)
					if c:
						d = zip(a)
						print ("\033[92m[✓] File :",d.filename)
						print ("\033[92m[✓] Path :",realpath(d.filename))
						for x in d.namelist():
							print ('\033[92m[✓]',x)
							d.extract(x)
						break
					else:
						exit('\033[94m[\033[91m!\033[94m] \033[93mGAGAL MENGAKSES',b)
				else:
					exit('\033[94m[\033[91m!\033[94m] \033[93mTERJADI KESALAHAN')
			elif v== 1:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 2:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v == 3:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 4:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 5:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 6:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 7:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 8:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 9:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 10:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 11:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 12:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 13:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 14:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 15:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 16:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 17:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 18:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 19:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 20:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 21:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 22:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 23:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 24:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 25:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 26:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 27:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 28:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 29:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 30:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 31:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 32:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 33:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 34:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 35:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 36:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 37:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 38:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 39:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 40:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 41:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 42:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 43:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 44:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 45:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 46:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 47:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 48:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 49:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 50:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 51:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v == 52:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v == 53:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v == 54:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v == 55:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v == 56:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 57:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v== 58:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			elif v==59:
				get(f"https://rahmat232.000webhostapp.com/v{v}.txt",f"v{v}.txt")
				main()
			else:
				print (f"\033[1;93m[!] KATA KUNCI DARI\033[1;96m {v} \033[1;93mTIDAK DI TEMUKAN!..")
				sleep(1.5)
		except ValueError:
			print ("\033[1;93m[!] INPUT BERUPA ANGKA")
			sleep(1.5)

#REPORT BUG & SARAN 
def bug2():
	sys('clear')
	try:
		print (logo)
		print ("\033[1;93mLAPOR MELALUI:")
		print (37* '\033[1;92m=')
		print ("\033[1;94m[\033[1;91m1\033[1;94m] \033[1;92mREPORT VIA WHATSAPP")
		print ("\033[1;94m[\033[1;91m2\033[1;94m] \033[1;96mREPORT VIA Facebook")
		print ("\033[1;94m[\033[1;91m0\033[1;94m] \033[1;91mKEMBALI")
		mail = int(input("\033[1;96m>>>>\033[1;94m "))
		if mail == 1:
			sys('clear')
			web('https://wa.me/6285754629509')
			bug2()
		elif mail == 2:
			sys('clear')
			web('https://www.facebook.com/profile.php?id=100053033144051')
			bug2()
		elif mail == 0:
			menu()
		else:
			print ("\033[1;93m[!] ISI YANG BENAR SAYANG KU!..")
			sleep(1.5)
			bug2()
	except ValueError:
		print ("\033[1;93m[!] INPUT BERUPA ANGKA")
		sleep(1.5)
		bug2()

#MENU UTAMA
def menu():
	try:
		sys('clear')
		print (logo)
		print ("\033[1;92mMENU UTAMA")
		print (37*'\033[1;96m=')
		print ('\033[94m[\033[93m1\033[94m] \033[92mDOWNLOAD FILE VIRTEX\n\033[94m[\033[93m2\033[94m] \033[93mLAPORKAN BUG\n\033[94m[\033[93m3\033[94m] \033[93mABOUT\n\033[94m[\033[93m0\033[94m] \033[91mKELUAR')
		nu = int(input("\033[1;93m>>>> \033[1;96m"))
		if nu == 1:
			main()
		elif nu == 2:
			bug2()
		elif nu == 3:
			sys('clear')
			print (f"{logo}\n\033[92mINFO SCRIPT\n========================\n\033[94m[\033[93m✓\033[94m] \033[96mAuthor: \033[92mRahmat adha\n\033[94m[\033[93m✓\033[94m] \033[96mTeam  : {warna()}TNT {warna()}ANONYMOUS \033[91mINDO\033[97mNESIA\n\033[94m[\033[93m✓\033[94m] \033[96mScript: {warna()}{basename(argv[0])}\n\033[94m[\033[93m✓\033[94m] \033[96mPath  : {realpath(argv[0])}\n\033[94m[\033[93m✓\033[94m] \033[96mSize  : {file_size(realpath(argv[0]))}\n\033[94m[\033[93m✓\033[94m] \033[96mLink  : {warna()}https://github.com/MR-X-Junior/Virtex\n\033[94m[\033[93m✓\033[94m] \033[96mUpdate: {warna()}{UPDATE}\n\033[94m[\033[93m✓\033[94m] \033[96mVersi : 1.0\n\n\033[92mContact Me ^_^\n==================\n\033[94m[\033[93m✓\033[94m] \033[96mGithub: {warna()}https://github.com/MR-X-Junior/\n\033[94m[\033[93m✓\033[94m] \033[96mFb.   : {warna()}https://www.facebook.com/Anjay.pro098\n\033[94m[\033[93m✓\033[94m] \033[96mWa.   : {warna()}+62 85754629509\n\033[94m[\033[93m✓\033[94m] \033[96mEmail : {warna()}termux.indonesia01@gmail.com\n")
		elif nu == 0:
			exit()
		else:
			print (f"\033[1;93m[!] KATA KUNCI DARI\033[1;96m {nu} \033[1;93mTIDAK DI TEMUKAN!..")
			sleep(1.5)
			menu()
	except (EOFError , KeyboardInterrupt):
		exit('exit')
	except ValueError:
		print ("\033[1;93m[!] INPUT BERUPA ANGKA")
		menu()

if __name__=="__main__":
	menu()
