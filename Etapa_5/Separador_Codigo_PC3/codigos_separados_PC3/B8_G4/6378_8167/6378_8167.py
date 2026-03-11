from numpy import *

s = input("Informe as notas retiradas pelos clientes: ").upper().split(",")

v = zeros(4,dtype=int)

for i in range(len(s)):
	if s[i] == "C":
		v[0] = v[0]+1
		
	elif s[i] == "D":
		v[1] = v[1]+1
		
	elif s[i] == "V":
		v[2] = v[2]+1
		
	elif s[i] == "U":
		v[3] = v[3]+1
		
print(v)