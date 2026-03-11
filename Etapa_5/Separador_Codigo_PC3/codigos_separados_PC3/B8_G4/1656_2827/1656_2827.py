from numpy import *

s = input("").upper().split(",")

be = 0
es = 0
fr = 0
it = 0
pt = 0

for i in range(size(s)):
	if s[i] == "BE":
		be = be + 1
	elif s[i] == "ES":
		es = es + 1
	elif s[i] == "FR":
		fr = fr + 1
	elif s[i] == "IT":
		it = it + 1
	elif s[i] == "PT":
		pt = pt + 1 
		
vz = zeros(5, dtype=int)

vz[0] = be
vz[1] = es
vz[2] = fr
vz[3] = it
vz[4] = pt

print(max(vz))
print(vz)



