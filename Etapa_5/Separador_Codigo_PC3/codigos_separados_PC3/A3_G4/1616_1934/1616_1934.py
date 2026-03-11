from numpy import *

tipo = array(eval(input("Tipos: ")))
nivel = array(eval(input("Nivel: ")))

i = 0
dano = 0

while(size(tipo) != i):
	if(tipo[i].upper() == "GELO"):
		d = 2
	if(tipo[i].upper() == "FOGO"):
		d = 3
	if(tipo[i].upper() == "CHOQUE"):
		d = 4
	if(tipo[i].upper() == "CONJURACAO"):
		d = 8
	if(tipo[i].upper() == "ILUSAO"):
		d = 10
	dano = dano + d * int(nivel[i])
	i = i + 1
print(int(dano))