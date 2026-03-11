from numpy import *

s = input("").upper().split(',')

AR= 0
BR= 0
CL= 0
CO= 0
UY= 0

for i in range(size(s)):
	if s[i] == "AR":
		AR = AR + 1
	elif s[i] == "BR":
		BR = BR + 1
	elif s[i] == "CL":
		CL = CL + 1
	elif s[i] == "CO":
		CO = CO + 1
	elif s[i] == "UY":
		UY = UY + 1
		
vz = zeros(5,dtype=int)

vz[0] = AR
vz[1] = BR
vz[2] = CL
vz[3] = CO
vz[4] = UY
print(max(vz))
print(vz)
