import os
import zlib

logo=(f"""
   >>> Welcome to DECODE & ENCODE TOOS>>>
   
 ----------------------------------------------------------
 [×] developer : Yasin Arafat
 [×] github  : AHMED-143
 [×] Tools : zlib,decompress
 ----------------------------------------------------------""")
print(logo)
def clear():
	os.system('clear')
	print(logo)
 
def main():
	print(' [1] zlib Text Decode ')
	print(' [2] zlib Text Encode ')
	print(' ')
	yasin=input(' Choice menu > ')
	if yasin in ['1']:
		decode()
	elif yasin in ['2']:
		encode()
	else:
		exit()
		
		

def decode():
	clear()
	put=input(' put text here > ')
	main=eval(put)
	dec=zlib.decompress(main)
	print(dec.decode('utf-8'))
	

def encode():
	clear()
	put=input(' PUT TEXT HERE > ')
	byte = put.encode('utf-8')
	compile = zlib.compress(byte)
	print(compile)

main()