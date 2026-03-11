from numpy import *
s= input("Digite a cor: ").upper().split(",")

cont= zeros(5, dtype=int)

for i in range(len(s)):
	if s[i] == "P":
		cont[0]= cont[0] + 1
	elif s[i] == "C":
		cont[1]= cont[1] + 1
	elif s[i] == "M":
		cont[2]= cont[2] + 1
	elif s[i] == "V":
		cont[3]= cont[3] + 1
	elif s[i] == "A":
		cont[4]= cont[4] + 1
print(max(cont))	
print(cont)