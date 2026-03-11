from numpy import *

notas = array(eval(input("Coloque suas notas:")))
peso = [1,3,2,5]

i = 0
t = len(notas) -1
s = 0
while i <= t:
	s += notas[i]*peso[i]
	i += 1
m = s/sum(peso)
print(round(m, 2))