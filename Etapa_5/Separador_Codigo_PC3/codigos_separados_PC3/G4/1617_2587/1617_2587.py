from numpy import *
string = array(eval(input("")))
n = array(eval(input("")))
i = 0
dano = 0
while(i < size(n)):
	if((string[i].lower() == "cenoura") or (string[i].lower() == "ferro") or (string[i].lower() == "dwarven") or (string[i].lower() == "elven") or (string[i].lower() == "daedric")):
		if(string[i].lower() == "cenoura"):
			dano = dano + 2 * n[i]
		elif(string[i].lower() == "ferro"):
			dano = dano + 4 * n[i]
		elif(string[i].lower() == "dwarven"):
			dano = dano + 8 * n[i]
		elif(string[i].lower() == "elven"):
			dano = dano + 11 * n[i]
		else:
			dano = dano + 14 * n[i]
	i = i + 1	
print(dano)