from numpy import *
s = array(eval(input()))
v = array(eval(input()))
i = 0
dano = 0

while(i<size(s)):
	if(s[i]=="CENOURA"):
		dano = dano+2*v[i]
	elif(s[i]=="FERRO"):
		dano = dano+4*v[i]
	elif(s[i]=="DWARVEN"):
		dano = dano+8*v[i]
	elif(s[i]=="ELVEN"):
		dano = dano+11*v[i]
	elif(s[i]=="DAEDRIC"):
		dano = dano+14*v[i]
	i = i+1
print(dano)

