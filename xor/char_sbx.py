import binascii
ct_enc="aÁh»öo:¥ì6Ñ×kT:4¡9ÐEÍ"

for i in range(256):
	flag=''
	for j in range(len(ct_enc)):
		flag+=chr(ord(ct_enc[j])^i)
	print(flag)

