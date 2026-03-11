from numpy import *

ataque = array(eval(input("Dano: ")))

i = 0
cont = 0

while (i < size(ataque)):
	cont = cont + 1
	i = i + 1
	peso = ataque[i] * i
print(peso)