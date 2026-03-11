from numpy import *

magia = array(eval(input()))
nivel = array(eval(input()))
i = 0
dano = 0

while i < len(magia):
	if str(magia[i]) == "GELO":
		dano_da_magia = 2
	elif str(magia[i]) == "FOGO":
		dano_da_magia = 3
	elif str(magia[i]) == "CHOQUE":
		dano_da_magia = 4	
	elif str(magia[i]) == "CONJURACAO":
		dano_da_magia = 8
	elif str(magia[i]) == "ILUSAO":
		dano_da_magia = 10
	dano = dano + dano_da_magia * float(nivel[i])
	i = i + 1
print(dano)