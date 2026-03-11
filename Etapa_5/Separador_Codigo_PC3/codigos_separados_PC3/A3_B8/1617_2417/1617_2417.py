from numpy import *
vetor_s = array(eval(input("")))
v = array(eval(input("")))
i = 0
dano = 0
while i < size(vetor_s) and i < size(v):
	if vetor_s[i] == "CENOURA":
		dano = 2
	elif vetor_s[i] == "FERRO":
		dano = dano + 4
	elif vetor_s[i] == "DWARVEN":	
		dano = dano + 8
	elif vetor_s[i] == "ELVEN":
		dano = dano + 11 
	elif vetor_s[i] == "DAEDRIC":
		dano = dano + 14
	
	dano_c = dano[dano] * v[i]
	i = i + 1
print(dano_c)