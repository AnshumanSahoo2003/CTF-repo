from pwn import *
import binascii
ct=binascii.unhexlify("4344495e4c5148194d1b44441b444d755d1b5e42755e4219755943475a4619595e57")
for i in range(256):
	key=chr(i)
	print(xor(ct,key))
