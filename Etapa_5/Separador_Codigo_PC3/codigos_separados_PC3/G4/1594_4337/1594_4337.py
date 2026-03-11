from numpy import *
n = array(eval(input()))

cont = 0
peso = 0
dano = 0

while(cont < size(n)):
	peso = peso + 1
	dano = dano + peso * (n[cont])
	cont = cont + 1
print(dano)