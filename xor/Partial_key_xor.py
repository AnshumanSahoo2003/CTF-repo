from pwn import *
ct="1^1]\Y#hb[etlDavwr<^aZiN"
key1="inctfj"
print(xor(ct,key1))
#output: b'X0R):3J\x06\x01/\x03\x1e\x05*\x02\x02\x11\x18U0\x02.\x0f$'
# we get a partial key now which is 'X0R):3'
key="X0R):3"
print(xor(ct,key))
#flag: inctfj{X0r_G4t3_MAdn3sS}