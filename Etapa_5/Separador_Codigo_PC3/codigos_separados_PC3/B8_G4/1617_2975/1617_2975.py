from numpy import *

s = array(eval(input()))
v = array(eval(input()))

dano = 0
i = 0
while (i<len(s)):
	
	if (s[i].upper() == "CENOURA"):
		
		dano = dano + (2 * v[i])
		
	elif(s[i].upper() == "FERRO"):
		
		dano = dano + (4 * v[i])
		
	elif(s[i].upper() == "DWARVEN"):
		
		dano = dano + (8 * v[i])
	elif(s[i].upper() == "ELVEN"):
		
		dano = dano + (11* v[i])
		
	elif(s[i].upper() == "DAEDRIC"):
		
		dano = dano + (14 * v[i])
		
	i = i + 1
	
print(dano)