from numpy import *
x = array(eval(input("")))
z = array(eval(input()))
#x = x.upper()
soma = 0
i = 0

while i < size(x):
	if x[i] == "GELO":
		dano = 2 
	elif x[i] == "FOGO":
		dano = 3
	elif x[i] == "CHOQUE":
		dano = 4
	elif x[i] == "CONJURACAO":
		dano = 8
	else:
		dano = 10 
	soma = soma + (dano * z[i])
	i = i + 1

print(soma)