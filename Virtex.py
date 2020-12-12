#coding=utf-8
import os,sys,time
from datetime import datetime

try:
	import requests
except ModuleNotFoundError:
	os.system('pip3 install requests')
	os.system('clear')

#TANGGAL RILIS 2020/08/18 19:51
#SENGAJA GAK DI ENSKRIPSI ^_^
#RECODE AJA GAK PAPA KOK ^_^

tabel="""╔═════════════════════════════════════╗\n║[•] Author : MR-X JUNIOR             ║\n║[•] GitHub : github.com/MR-X-Junior  ║\n║[•] WA.    : +6285754629509          ║\n║[•] UPDATE : 2020/08/18 19:51.       ║\n╚═════════════════════════════════════╝"""
menu2="""\033[1;94m[\033[1;91m1\033[1;94m] \033[1;92mDOWNLOAD FILE VIRTEX\n\033[1;94m[\033[1;91m2\033[1;94m] \033[1;96mUPGRADE KE BETA\n\033[1;94m[\033[1;91m3\033[1;94m] \033[1;93mLAPORKAN BUG\n\033[1;94m[\033[1;91m0\033[1;94m] \033[1;91mKELUAR"""
nama2ku="""\033[1;91m                                 \n@@@@@@@@@@   @@@@@@@      @@@  @@@  \n@@@@@@@@@@@  @@@@@@@@     @@@  @@@  \n@@! @@! @@!  @@!  @@@     @@!  !@@  \n!@! !@! !@!  !@!  @!@     !@!  @!!  \n@!! !!@ @!@  @!@!!@!       !@@!@!   \n!@!   ! !@!  !!@!@!         @!!!    \n!!:     !!:  !!: :!!       !: :!!   \n:!:     :!:  :!:  !:!     :!:  !:!  \n:::     ::   ::   :::      ::  :::  \n:      :     :   : :      :   ::                                  """
nama2="""\033[1;94m****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     // """
virtex="""\033[1;94m[\033[1;91m01\033[1;94m] \033[1;91m☕⇣፟፝P፟፝A፟፝፞N̩፟፝T፟፝፞A፟፝N፟፞፝G፟፝ ፟፝M፟፞፟፝U፟፞፝N፟፝D፟፝U፟፝R፟፝ 7̩፟፝6̩፟፝9 A፟፝N፟፞፝T፟፝I A፟፝P፟፞፝E፟፝S፟፝-1-1 \n\033[1;94m[\033[1;91m02\033[1;94m] \033[1;92m☞IPHONE KILLER☜ \n\033[1;94m[\033[1;91m03\033[1;94m] \033[1;93m☬.∆.G.I.N.☬.-1 \n\033[1;94m[\033[1;91m04\033[1;94m] \033[1;94m♞™CAVALO卐DE♞TROIA♞-1-1-2-1-1 \n\033[1;94m[\033[1;91m05\033[1;94m] \033[1;95m14N Virus \n\033[1;94m[\033[1;91m06\033[1;94m] \033[1;96mĐ.Δ.Μ.Ň.į.Ҝ.Δ.ᇸ-WPS Office\n\033[1;94m[\033[1;91m07\033[1;94m] \033[1;97mdamnika\n\033[1;94m[\033[1;91m08\033[1;94m] \033[1;91mDིྀuིྀeིྀtིྀmིྀaིྀuིྀtིྀ45\n\033[1;94m[\033[1;91m09\033[1;94m] \033[1;92mfunambol\n\033[1;94m[\033[1;91m10\033[1;94m] \033[1;93mGHOSTNAME VIRTEXT GANAS\n\033[1;94m[\033[1;91m11\033[1;94m] \033[1;94mGHOSTNAME VIRTEXT PART 2\n\033[1;94m[\033[1;91m12\033[1;94m] \033[1;95m🆔❗༺🔱🔱🔱♛R̸͟͞O̸͟͞K̸͟͞E̸͟͞T̸͟͞♛G̸͟͞H̸͟͞O̸͟͞S̸͟͞T̸͟͞♛🌀1⃣9⃣4 (1)\n\033[1;94m[\033[1;91m13\033[1;94m] \033[1;96mMR.KACANG\n\033[1;94m[\033[1;91m14\033[1;94m] \033[1;97mPantang\n\033[1;94m[\033[1;91m15\033[1;94m] \033[1;91mPilus\n\033[1;94m[\033[1;91m16\033[1;94m] \033[1;92mRayhan feat agus\n\033[1;94m[\033[1;91m17\033[1;94m] \033[1;93mrv\n\033[1;94m[\033[1;91m18\033[1;94m] \033[1;94mSerigala Hitam\n\033[1;94m[\033[1;91m19\033[1;94m] \033[1;95mVIP CODE LAG BY GHOSTNAME\n\033[1;94m[\033[1;91m20\033[1;94m] \033[1;96mVIRTEKS ALI BUKAN KALENG2\n\033[1;94m[\033[1;91m21\033[1;94m] \033[1;97mVirtex by habib [VG Cyber]\n\033[1;94m[\033[1;91m22\033[1;94m] \033[1;91mVirtex lol\n\033[1;94m[\033[1;91m23\033[1;94m] \033[1;92mV̤̈Ï̤R̤̈T̤̈Ë̤Ẍ̤T̤̈ B̤̈Ÿ̤ G̤̈Ḧ̤Ö̤S̤̈T̤̈N̤̈Ä̤M̤̈Ë̤ P̤̈Ä̤R̤̈T̤̈ 2\n\033[1;94m[\033[1;91m24\033[1;94m] \033[1;93mV̺͆I̺͆R̺͆T̺͆E̺͆X̺͆T̺͆ B̺͆Y̺͆ G̺͆H̺͆O̺͆S̺͆T̺͆N̺͆A̺͆M̺͆E̺͆\n\033[1;94m[\033[1;91m25\033[1;94m] \033[1;94mVIRTEXT DAMNIKA BARU\n\033[1;94m[\033[1;91m26\033[1;94m] \033[1;95mVIRTEXT KERAD BY GHOST NAME\n\033[1;94m[\033[1;91m27\033[1;94m] \033[1;96mVIRTEXT TESTER BY GHOSTNAME\n\033[1;94m[\033[1;91m28\033[1;94m] \033[1;97mvirus 1 TU4NB4ND1T\n\033[1;94m[\033[1;91m29\033[1;94m] \033[1;91mVIRUS BY GHOSTNAME\n\033[1;94m[\033[1;91m30\033[1;94m] \033[1;92mvirus gua Mr.H4R1\n\033[1;94m[\033[1;91m31\033[1;94m] \033[1;93mVIRUS LAG BY GHOSTNAME\n\033[1;94m[\033[1;91m32\033[1;94m] \033[1;94mVIRUS LAG WA\n\033[1;94m[\033[1;91m33\033[1;94m] \033[1;95mVIRUS LORD CHOKY\n\033[1;94m[\033[1;91m34\033[1;94m] \033[1;96mVIRUS MEMATIKAN BY GHOSTNAME\n\033[1;94m[\033[1;91m35\033[1;94m] \033[1;97mVIRUS MEMATIKAN BY RIZKY GEBOY VIRTEXT\n\033[1;94m[\033[1;91m36\033[1;94m] \033[1;91mVIRUS MEMATIKAN PART 2\n\033[1;94m[\033[1;91m37\033[1;94m] \033[1;92mVIRUS MEMATIKAN PART 3\n\033[1;94m[\033[1;91m38\033[1;94m] \033[1;93mVIRUS MEMATIKAN PART 4\n\033[1;94m[\033[1;91m39\033[1;94m] \033[1;94mVIRUS MEMATIKAN PART 5\n\033[1;94m[\033[1;91m40\033[1;94m] \033[1;95mVirus Mr.f4r!5\n\033[1;94m[\033[1;91m41\033[1;94m] \033[1;96mvirus si error\n\033[1;94m[\033[1;91m42\033[1;94m] \033[1;97mVIRUS TEXT TEST GHOSTNAME\n\033[1;94m[\033[1;91m43\033[1;94m] \033[1;91mvirus-1\n\033[1;94m[\033[1;91m44\033[1;94m] \033[1;92mvirus\n\033[1;94m[\033[1;91m45\033[1;94m] \033[1;93mvirus3ME\n\033[1;94m[\033[1;91m46\033[1;94m] \033[1;94mvirus4ME\n\033[1;94m[\033[1;91m47\033[1;94m] \033[1;95mvirushari2\n\033[1;94m[\033[1;91m48\033[1;94m] \033[1;96mVirusPending+Legh\n\033[1;94m[\033[1;91m49\033[1;94m] \033[1;97mVIRUSSETANOFFICIAL\n\033[1;94m[\033[1;91m50\033[1;94m] \033[1;91mVirusWaLag\n\033[1;94m[\033[1;91m51\033[1;94m] \033[1;95m🈴🈴🔝🔝🔝☬ŘÅJÃ⚔ŤĔŘØŘ♐8⃣7⃣9⃣♐☬🔝🔝🔝🈴🈴\n\033[1;94m[\033[1;91m52\033[1;94m] \033[1;96mUNDUH SEMUA VIRTEX\n\033[1;94m[\033[1;91m99\033[1;94m] \033[1;93mKEMBALI KE MENU UTAMA\n\033[1;94m[\033[1;91m00\033[1;94m] \033[1;91mKELUAR DARI PROGRAM"""

def keluar():
	os.system('clear')
	jalan ("\033[1;93m[?] UDAHAN NIH ?")
	time.sleep(3)
	jalan ("\033[1;92m[✓] MAKASIH YA KAK UDAH PAKE SCRIPTNYA ^_^")
	time.sleep(1)
	exit()

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def bug2():
	os.system('clear')
	print (nama2)
	print (tabel)
	time.sleep(3)
	print ("\033[1;93mLAPOR MELALUI:")
	print (37* '\033[1;92m=')
	print ("\033[1;94m[\033[1;91m1\033[1;94m] \033[1;94mREPORT VIA EMAIL")
	print ("\033[1;94m[\033[1;91m2\033[1;94m] \033[1;92mREPORT VIA WHATSAPP")
	print ("\033[1;94m[\033[1;91m3\033[1;94m] \033[1;96mREPORT VIA Facebook")
	print ("\033[1;94m[\033[1;91m0\033[1;94m] \033[1;91mKEMBALI")
	mail=input("\033[1;96m>>>>\033[1;94m ")
	if mail=="":
		jalan ("[!] MOHON ISI DENGAN BENAR")
		time.sleep(3)
		bug2()
	elif mail=="1" or mail=="01":
		os.system('clear')
		jalan ("[✓] SILAHKAN HUBUNGI SAYA MELALUI EMAIL DI BAWAH INI!!")
		print ("====================================================")
		print ("\033[1;92m1.hacked.by.mr.x232@gmail.com")
		print ("\033[1;95m==================================")
		print ("\033[1;93m2.anonymousindonesia232@gmail.com")
		print ("\033[1;95m==================================")
		jalan ("")
		time.sleep(2)
		input("[KEMBALI] ")
		bug2()
	elif mail=="2" or mail=="02":
		os.system('clear')
		time.sleep(2)
		os.system(' xdg-open https://wa.me/6285754629509')
		time.sleep(1)
		bug2()
	elif mail=="3" or mail=="03":
		os.system('clear')
		time.sleep(2)
		os.system('xdg-open https://www.facebook.com/profile.php?id=100053033144051')
		time.sleep(2)
		bug2()
	elif mail=="0" or mail=="00":
		menu()
	else:
		print ("\033[1;93m[!] ISI YANG BENAR SAYANG KU!..")
		time.sleep(4)
		bug2()

def menu():
	os.system('clear')
	print (nama2)
	print (tabel)
	print ("\033[1;92mMENU UTAMA")
	print (30*'\033[1;96m=')
	print (menu2)
	nu=input("\033[1;93m>>>> \033[1;96m")
	if nu=="":
		jalan ("\033[1;91m[!] ISI YANG BENAR SAYANG KU!..")
		time.sleep(4)
		menu()
	elif nu=="1" or nu=="01":
		virtex2()
	elif nu=="2" or nu=="02":
		BETA()
	elif nu=="3" or nu=="03":
		bug2()
	elif nu=="0" or nu=="00":
		keluar()
	else:
		jalan ("\033[1;93m[!] KATA KUNCI DARI\033[1;96m "+nu+ " \033[1;93mTIDAK DI TEMUKAN!..")
		time.sleep(3)
		menu()

def BETA():
	os.system('clear')
	try:
		print (nama2)
		print (tabel)
		print ("")
		print ('\033[92mUPGRADE KE VERSI BETA')
		print (25* '\033[97m=')
		a = input ('\033[93m[!] TEKAN \033[92mCTRL + C \033[93mUNTUK UPGRADE KE VERSI BETA\n[!] TEKAN ENTER UNTUK MEMBATALKAN PEMBARUAN ')
		if a == "":
			print ('\033[95m[!] DI BATALKAN')
			time.sleep(3)
			menu()
		else:
			print ('\033[93m[!] INPUT SALAH')
			time.sleep(2)
			BETA()
	except KeyboardInterrupt:
		os.system('wget https://raw.githubusercontent.com/MR-X-junior/Virtex-Beta/main/Data.py')
		os.system('wget https://raw.githubusercontent.com/MR-X-junior/Virtex-Beta/main/bahan.py')
		os.system('clear')
		print ('\033[92m[✓] MEMULAI PROSES')
		time.sleep(3)
		try:
			from time import sleep as a
			from os import system as b
			b('clear')
			print (nama2)
			print (tabel)
			print ('\033[96mMENDOWNLOAD FILE')
			print (25* '\033[92m=')
			sekarang = datetime.now()

			hari = sekarang.day

			bulan = sekarang.month
			
			tahun = sekarang.year
			
			jam = sekarang.hour
			
			menit = sekarang.minute
			
			detik = sekarang.second

			print (f'\033[93m[!] UNDUHAN DI MULAI PADA \033[92m{hari}\033[95m-\033[93m{bulan}\033[95m-\033[94m{tahun} \033[96m{jam}\033[95m:\033[97m{menit}\033[95m:\033[92m{detik}')
			a(3)
			url = 'https://raw.githubusercontent.com/MR-X-junior/Virtex-Beta/main/Virtex_BETA.py'
			r = requests.get(url)
			filename = url.split('/')[-1]
			with open(filename, 'wb') as out_file:
				out_file.write(r.content)
			sekarang2 = datetime.now()

			hari2 = sekarang.day

			bulan2 = sekarang.month
			
			tahun2 = sekarang.year
			
			jam2 = sekarang.hour
			
			menit2 = sekarang.minute
			
			detik2  = sekarang.second
			try:
				import Virtex_BETA
				print (f'\033[92m[✓] UNDUHAN SELESAI PADA \033[92m{hari2}\033[95m-\033[93m{bulan2}\033[95m-\033[94m{tahun2} \033[96m{jam2}\033[95m:\033[97m{menit2}\033[95m:\033[92m{detik2}')
				a(2)
			except ModuleNotFoundError:
				exit('\033[91m[!] GAGAL MENDOWNLOAD FILE')
			try:
				print ('\033[93m[!] MEMERIKSA FILE\n')
				a(2)
				b('ls')
				from Virtex_BETA import dukung_author
			except ModuleNotFoundError:
				exit ('\033[91m[!] ADA YANG TIDAK BERES')
			except ImportError:
				exit('\033[93m[!] IMPORT ERROR')
			print ('\033[92m[✓] MENGINSTAL BAHAN')
			a(4)
			b('python bahan.py')
			exit('\n\033[92m[✓] FILE : \033[93mVirtex_BETA.py \033[92mSIAP DI GUNAKAN')
		except KeyboardInterrupt:
			print ('\033[93m[!] UNDUHAN DI BATALKAN')
			a(2)
			menu()
		except PermissionError:
			exit('\033[91m[!] GAGAL MENGAKSES PENYIMPANAN')
			

def virtex2():
	os.system('clear')
	print (nama2)
	print (tabel)
	print("")
	print ("\033[1;92mPILIH JENIS VIRTEX")
	print (43*'\033[1;96m=')
	print (virtex)
	v=input("\033[1;92m>>>> \033[1;96m")
	if v=="":
		jalan ("\033[1;91m[!] MOHON ISI DENGAN BENAR!..")
		time.sleep(3)
		virtex2()
	elif v=="99":
		os.system('clear')
		menu()
	elif v=="00" or v=="0":
		keluar()
	elif v=="52":
		jalan ("\033[1;93m[!] DOWNLOADING FILE!..")
		time.sleep(2)
		os.system('git clone https://github.com/MR-X292/virtex')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		time.sleep(2)
		input ("\033[1;93m[ KEMBALI ]")
		virtex2()
	elif v=="1" or v=="01":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/☕⇣፟፝P፟፝A፟፝፞N̩፟፝T፟፝፞A፟፝N፟፞፝G፟፝%20፟፝M፟፞፟፝U፟፞፝N፟፝D፟፝U፟፝R፟፝%207̩፟፝6̩፟፝9%20A፟፝N፟፞፝T፟፝I%20A፟፝P፟፞፝E፟፝S፟፝-1-1.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		time.sleep(1)
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="2" or v=="02":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/☞IPHONE%20KILLER☜.txt')
		time.sleep(1)
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="3" or v=="03":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/☬.∆.G.I.N.☬.-1.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		time.sleep(1)
		input ("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="4" or v=="04":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/♞™CAVALO卐DE♞TROIA♞-1-1-2-1-1.txt')
		time.sleep(1)
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="05" or v=="5":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/14N%20Virus.txt')
		time.sleep(1)
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		time.sleep(1)
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="6" or v=="06": 
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Đ.Δ.Μ.Ň.į.Ҝ.Δ.ᇸ-WPS%20Office.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		time.sleep(1)
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="07" or v=="7":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/damnika.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		time.sleep(1)
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="8" or v=="08":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Dིྀuིྀeིྀtིྀmིྀaིྀuིྀtིྀ45.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input ("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="9" or v=="09":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/funambol.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		time.sleep(1)
		input("\033[1;95m[ KEMBALI ] ")
		virtex2()
	elif v=="10":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/GHOSTNAME%20VIRTEXT%20GANAS.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="11":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/GHOSTNAME%20VIRTEXT%20PART%202.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="12":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/🆔❗༺🔱🔱🔱♛R̸͟͞O̸͟͞K̸͟͞E̸͟͞T̸͟͞♛G̸͟͞H̸͟͞O̸͟͞S̸͟͞T̸͟͞♛🌀1⃣9⃣4%20(1).txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!.")
		time.sleep(1)
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="13":
		jalan("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/MR.KACANG.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!.")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="14":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Pantang.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="15":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Pilus.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="16":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Rayhan%20feat%20agus.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="17":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/rv.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="18":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Serigala%20Hitam.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="19":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIP%20CODE%20LAG%20BY%20GHOSTNAME.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="20":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRTEKS%20ALI%20BUKAN%20KALENG2.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="21":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Virtex%20by%20habib%20[VG%20Cyber].txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="22":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Virtex%20Lol.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="23":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/V̤̈Ï̤R̤̈T̤̈Ë̤Ẍ̤T̤̈%20B̤̈Ÿ̤%20G̤̈Ḧ̤Ö̤S̤̈T̤̈N̤̈Ä̤M̤̈Ë̤%20P̤̈Ä̤R̤̈T̤̈%202.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="24":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/V̺͆I̺͆R̺͆T̺͆E̺͆X̺͆T̺͆%20B̺͆Y̺͆%20G̺͆H̺͆O̺͆S̺͆T̺͆N̺͆A̺͆M̺͆E̺͆.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="25":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRTEXT%20DAMNIKA%20BARU.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="26":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRTEXT%20KERAD%20BY%20GHOST%20NAME.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="27":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRTEXT%20TESTER%20BY%20GHOSTNAME.TXT')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="28":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/virus%201%20TU4NB4ND1T.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="29":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20BY%20GHOSTNAME.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="30":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/virus%20gua%20Mr.H4R1.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="31":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20LAG%20BY%20GHOSTNAME.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="32":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20LAG%20WA.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="33":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20LORD%20CHOKY.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="34":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20MEMATIKAN%20BY%20GHOSTNAME.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="35":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20MEMATIKAN%20BY%20RIZKY%20GEBOY%20VIRTEXT.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="36":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20MEMATIKAN%20PART%202.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="37":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20MEMATIKAN%20PART%203.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="38":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20MEMATIKAN%20PART%204.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="39":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20MEMATIKAN%20PART%205.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="40":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Virus%20Mr.f4r!5.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="41":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/virus%20si%20error.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="42":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUS%20TEXT%20TEST%20GHOSTNAME.TXT')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="43":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/virus-1.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="44":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/virus.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="45":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/virus3Me.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="46":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/Virus4Me.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="47":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/virushari2.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="48":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VirusPending%2BLegh.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="49":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VIRUSSETANOFFICIAL.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="50":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/VirusWaLag-1.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	elif v=="51":
		jalan ("\033[1;93m[✓] MENDOWNLOAD FILE!..")
		time.sleep(2)
		os.system('wget https://raw.githubusercontent.com/MR-X292/virtex/master/🈴🈴🔝🔝🔝☬ŘÅJÃ⚔ŤĔŘØŘ♐8⃣7⃣9⃣♐☬🔝🔝🔝🈴🈴.txt')
		jalan ("\033[1;92m[✓] DOWNLOAD SELESAI!..")
		input("\033[1;95m[ KEMBALI ]")
		virtex2()
	else:
		jalan ("\033[1;93m[!] KATA KUNCI DARI\033[1;96m "+v+ " \033[1;93mTIDAK DI TEMUKAN!..")
		time.sleep(4)
		virtex2()

if __name__=="__main__":
	menu()
