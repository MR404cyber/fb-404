import sys
if sys.version_info.major != 3:
	exit("{}[!] Kamu Menggunakan Python Versi {}\n[!] Harap Gunakan Python Versi 3\n[+] Silahkan Untuk Mengketikan python3 {}".format("\x1b[1;31m",sys.version_info.major,sys.argv[0]))
if __name__=="__main__":
	from piton3 import menu
	menu()
