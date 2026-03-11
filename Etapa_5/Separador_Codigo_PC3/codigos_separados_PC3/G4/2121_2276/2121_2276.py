from numpy import *
notas = array(eval(input()))
p = notas[0]
s = notas[1]
t = notas[2]
x = (p*5 + s* 3 + t*2)/10
if x >= 5:
	print(round(x, 2))
	print("APROVADO")
else:
	print(round(x, 2))
	print("REPROVADO")