# faça seu código aqui!
from numpy import *
c = input('insira um numero: ').upper()
i = 0
cont = 0

while i < len(c):
	if c [i] == "C":
		cont += 1
	i += 1

print(cont)

