#coding=utf-8
import os
import sys
import time
import random
import socket
import zipfile
import webbrowser

from urllib.request import urlopen as request
from urllib.error import URLError as SocketError

if 'linux' in sys.platform:
  r = "\033[91m" # Red
  g = "\033[92m" # Green
  y = "\033[93m" # Yellow
  p = "\033[94m" # Purple
  P = "\033[95m" # Pink
  c = "\033[96m" # Cyan
  w = "\033[97m" # White
  a = "\033[0m"  # Reset
else:
  # Convert String To Variabel Name
  for i in ['r','g','y','p','P','c','w','a']:
    globals()[i] = ""

# Last Update
UPDATE = "07-07-2021 19:26"

# Random ANSI Code
colors = lambda : random.choice([r,g,y,p,P,c,w])

#
add = [i for i in range(1,60)]

# Logo
logo = f"{r}****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n{p}╔═════════════════════════════════════╗\n║[{y}•{p}] {c}Author : {g}MR-X JUNIOR             {p}║\n║[{y}•{p}] {c}GitHub : {w}github.com/MR-X-Junior  {p}║\n║[{y}•{p}] {c}WA.    : {y}+62 85754629509        {p} ║\n║[{y}•{p}] {c}UPDATE : {UPDATE}      {p}  ║\n║[{y}•{p}] {c}Python : {colors()}{sys.version[0:6]}                {p}  ║\n║[{y}•{p}] {c}OS     : {colors()}{sys.platform}{' '*(23 - len(sys.platform))}{p} ║\n║[{y}•{p}] {c}Host   : {colors()}{socket.gethostname()}{' '*(24 - len(socket.gethostname()))}{p}║\n║[{y}•{p}] {c}Team.  : {colors()}TNT {colors()}ANONYMOUS {r}INDO{w}NESIA{p} ║\n╚═════════════════════════════════════╝{a}"

# Virtex Menu
virtex= f"""{p}[{r}01{p}] {r}☕⇣፟፝P፟፝A፟፝፞N̩፟፝T፟፝፞A፟፝N፟፞፝G፟፝ ፟፝M፟፞፟፝U፟፞፝N፟፝D፟፝U፟፝R፟፝ 7̩፟፝6̩፟፝9 A፟፝N፟፞፝T፟፝I A፟፝P፟፞፝E፟፝S፟፝-1-1 \n{p}[{r}02{p}] {g}☞IPHONE KILLER☜ \n{p}[{r}03{p}] {y}☬.∆.G.I.N.☬.-1 \n{p}[{r}04{p}] {p}♞™CAVALO卐DE♞TROIA♞-1-1-2-1-1 \n{p}[{r}05{p}] {P}14N Virus \n{p}[{r}06{p}] {c}Đ.Δ.Μ.Ň.į.Ҝ.Δ.ᇸ-WPS Office\n{p}[{r}07{p}] {w}damnika\n{p}[{r}08{p}] {r}Dིྀuིྀeིྀtིྀmིྀaིྀuིྀtིྀ45\n{p}[{r}09{p}] {g}funambol\n{p}[{r}10{p}] {y}GHOSTNAME VIRTEXT GANAS\n{p}[{r}11{p}] {p}GHOSTNAME VIRTEXT PART 2\n{p}[{r}12{p}] {P}🆔❗༺🔱🔱🔱♛R̸͟͞O̸͟͞K̸͟͞E̸͟͞T̸͟͞♛G̸͟͞H̸͟͞O̸͟͞S̸͟͞T̸͟͞♛🌀1⃣9⃣4 (1)\n{p}[{r}13{p}] {c}MR.KACANG\n{p}[{r}14{p}] {w}Pantang\n{p}[{r}15{p}] {r}Pilus\n{p}[{r}16{p}] {g}Rayhan feat agus\n{p}[{r}17{p}] {y}rv\n{p}[{r}18{p}] {p}Serigala Hitam\n{p}[{r}19{p}] {P}VIP CODE LAG BY GHOSTNAME\n{p}[{r}20{p}] {c}VIRTEKS ALI BUKAN KALENG2\n{p}[{r}21{p}] {w}Virtex by habib [VG Cyber]\n{p}[{r}22{p}] {r}Virtex lol\n{p}[{r}23{p}] {g}V̤̈Ï̤R̤̈T̤̈Ë̤Ẍ̤T̤̈ B̤̈Ÿ̤ G̤̈Ḧ̤Ö̤S̤̈T̤̈N̤̈Ä̤M̤̈Ë̤ P̤̈Ä̤R̤̈T̤̈ 2\n{p}[{r}24{p}] {y}V̺͆I̺͆R̺͆T̺͆E̺͆X̺͆T̺͆ B̺͆Y̺͆ G̺͆H̺͆O̺͆S̺͆T̺͆N̺͆A̺͆M̺͆E̺͆\n{p}[{r}25{p}] {p}VIRTEXT DAMNIKA BARU\n{p}[{r}26{p}] {P}VIRTEXT KERAD BY GHOST NAME\n{p}[{r}27{p}] {c}VIRTEXT TESTER BY GHOSTNAME\n{p}[{r}28{p}] {w}virus 1 TU4NB4ND1T\n{p}[{r}29{p}] {r}VIRUS BY GHOSTNAME\n{p}[{r}30{p}] {g}virus gua Mr.H4R1\n{p}[{r}31{p}] {y}VIRUS LAG BY GHOSTNAME\n{p}[{r}32{p}] {p}VIRUS LAG WA\n{p}[{r}33{p}] {P}VIRUS LORD CHOKY\n{p}[{r}34{p}] {c}VIRUS MEMATIKAN BY GHOSTNAME\n{p}[{r}35{p}] {w}VIRUS MEMATIKAN BY RIZKY GEBOY VIRTEXT\n{p}[{r}36{p}] {r}VIRUS MEMATIKAN PART 2\n{p}[{r}37{p}] {g}VIRUS MEMATIKAN PART 3\n{p}[{r}38{p}] {y}VIRUS MEMATIKAN PART 4\n{p}[{r}39{p}] {p}VIRUS MEMATIKAN PART 5\n{p}[{r}40{p}] {P}Virus Mr.f4r!5\n{p}[{r}41{p}] {c}virus si error\n{p}[{r}42{p}] {w}VIRUS TEXT TEST GHOSTNAME\n{p}[{r}43{p}] {r}virus-1\n{p}[{r}44{p}] {g}virus\n{p}[{r}45{p}] {y}virus3ME\n{p}[{r}46{p}] {p}virus4ME\n{p}[{r}47{p}] {P}virushari2\n{p}[{r}48{p}] {c}VirusPending+Legh\n{p}[{r}49{p}] {w}VIRUSSETANOFFICIAL\n{p}[{r}50{p}] {r}VirusWaLag\n{p}[{r}51{p}] {P}🈴🈴🔝🔝🔝☬ŘÅJÃ⚔ŤĔŘØŘ♐8⃣7⃣9⃣♐☬🔝🔝🔝🈴🈴\n{p}[{r}52{p}] {g}ATTACKER ALON\n{p}[{r}53{p}] {y}FrezzN00b\n{p}[{r}54{p}] {p}HekelKokUnicodeByFrezz\n{p}[{r}55{p}] {P}Kode Lag ★ISL★-1-1-1-1\n{p}[{r}56{p}] {c}Nyai•Annah\n{p}[{r}57{p}] {w}SCRIPT~WHATSAPP\n{p}[{r}58{p}] {r}Serigala Hitam\n{p}[{r}59{p}] {g}VIRτΣXGΔПΔς\n{p}[{r}60{p}] {c}UNDUH SEMUA VIRTEX\n{p}[{r}99{p}] {y}KEMBALI KE MENU UTAMA\n{p}[{r}00{p}] {r}KELUAR DARI PROGRAM{a}"""


# Download File
def Download(path):
  total = 0
  print ("%s[%s!%s] %sDownloading %s%s%s" % (p,y,p,y,c,path,a))
  while 1:
    try:
      data = request("https://rahmat232.000webhostapp.com/"+path)
      print ("%s[%s✓%s] %sURL : %s" % (p,y,p,y,data.geturl()))
      print ("%s[%s✓%s] %sStatus : %s" % (p,y,p,y,data.status))
      fopen = os.open(path,os.O_WRONLY | os.O_CREAT)
      os.write(fopen,data.read())
      os.close(fopen)
      print ("%s[%s✓%s] %sFile Name : %s" % (p,y,p,g,os.path.basename(path)))
      byte = os.stat(path).st_size
      for b in ['B','KB','MB','GB','TB']:
        if byte < 1024.0:
          byte = "%3.1f %s" % (byte,b)
          break
        else:
          byte /= 1024.0
      print ("%s[%s✓%s] %sFile Size : %s" % (p,y,p,g,byte))
      print ("%s[%s✓%s] %sFile Path : %s" % (p,y,p,g,os.path.realpath(path)))
      var = input('%s[%s?%s] %sLihat Hasil Download [%sY%s/%sn%s]%s ' % (p,y,p,w,g,w,r,w,P)).lower()
      if var == 'y':
        os.system ("xdg-open --view "+path)
        break
      else:
        break
    except SocketError as Soc:
      total += 1
      if total == 5:
        print ("%s[%s!%s] %sGagal Terhubung Ke Server\n\n\tCoba :\n\t\t• Nonaktifkan mode pesawat\n\t\t• Aktifkan data seluler atau Wi-Fi\n\t\t• Periksa sinyal di area Anda\n%s%s" % (p,y,p,y,Soc,a))
        exit()
      else:
        print ("%s[%s!%s] %sMencoba menghubungkan ulang ke server" % (p,y,p,y))
        time.sleep(1.5)

# Main Program
def main():
   while 1:
    os.system('clear')
    print (logo)
    try:
      print ("%sPILIH JENIS VIRTEX" % (g))
      print ("%s%s%s" % (c,'='*43,a))
      print (virtex)
      v = int(input("%s>>>> %s" % (g,c)))
      if v == 99:
        menu() ; break
      elif v == 0:
        os.abort()
      elif v == 60:
        try:
          print ("%s[%s!%s] %sDownloading virtex-master.zip" % (p,y,p,y))
          data = request("https://rahmat232.000webhostapp.com/virtex-master.zip").read()
          shifa = os.open("virtex-master.zip",os.O_WRONLY | os.O_CREAT)
          os.write(shifa,data)
          os.close(shifa)
          zip = zipfile.ZipFile("virtex-master.zip")
          print ("%s[✓] File Name : %s" % (g,zip.filename))
          print ("%s[✓] File Path : %s" % (g,os.path.realpath(zip.filename)))
          for file in zip.namelist():
            zip.extract(file)
            print ("%s[✓] %s" % (g,file))
          else:
            print (r + "[!] Exit!")
            break
        except SocketError:
          print ("%s[%s!%s] %sTidak Ada Koneksi%s" % (p,y,p,y,a))
          break
      elif v in add:
        Download("v%d.txt" % (v))
      else:
        raise ValueError
    except ValueError:
      print ("%s[!] Invalid Input!" % (y))
      time.sleep(1.5)

# Menu
def menu():
  os.system('clear')
  print (logo)
  print (g + "MENU UTAMA")
  print ("%s%s" % (c,"="*37))
  print (f'{p}[{y}1{p}] {g}DOWNLOAD FILE VIRTEX\n{p}[{y}2{p}] {y}LAPORKAN BUG\n{p}[{y}3{p}] {y}ABOUT\n{p}[{y}0{p}] {r}KELUAR')
  choice = input("%s>>> %s" % (y,c))
  if choice == '1' or choice == '01':
    main()
  elif choice == '2' or choice == '02':
    url = "https://wa.me/6285754629509"
    code = webbrowser.open(url)
    if code:
      time.sleep(0.9)
      memu()
    else:
      os.system ("xdg-open "+url)
  elif choice == '3' or choice == '03':
    os.system('clear')
    print (f"{logo}\n{g}INFO SCRIPT\n========================\n{p}[{y}✓{p}] {c}Author: {g}Rahmat adha\n{p}[{y}✓{p}] {c}Team  : {colors()}TNT {colors()}ANONYMOUS {r}INDO{w}NESIA\n{p}[{y}✓{p}] {c}Script: {colors()}{os.path.basename(sys.argv[0])}\n{p}[{y}✓{p}] {c}Path  : {os.path.realpath(sys.argv[0])}\n{p}[{y}✓{p}] {c}Size  : {os.stat(os.path.realpath(sys.argv[0])).st_size} Byte\n{p}[{y}✓{p}] {c}Link  : {colors()}https://github.com/MR-X-Junior/Virtex\n{p}[{y}✓{p}] {c}Update: {colors()}{UPDATE}\n{p}[{y}✓{p}] {c}Versi : 1.1\n\n{g}Contact Me ^_^\n==================\n{p}[{y}✓{p}] {c}Github: {colors()}https://github.com/MR-X-Junior/\n{p}[{y}✓{p}] {c}Fb.   : {colors()}https://www.facebook.com/Anjay.pro098\n{p}[{y}✓{p}] {c}Wa.   : {colors()}+62 85754629509\n{p}[{y}✓{p}] {c}Email : {colors()}termux.indonesia01@gmail.com\n{a}")
  elif choice == '00' or choice == '0':
    os.abort()
  else:
    print ("%s[!] Invalid Input!" % (y))
    time.sleep(0.9)
    menu()

if __name__ == "__main__":
  menu()
