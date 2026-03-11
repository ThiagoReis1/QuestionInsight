from numpy import *

nomes = array(eval(input()))
dur = array(eval(input()))

soma = 0

i=0

while i < size(nomes):
	if nomes[i] == "ALONGAMENTO":
		soma = dur[i] * 3 + soma
	elif nomes[i] == "CORRIDA":
		soma = dur[i] * 10.3 + soma
	elif nomes[i] == "DANCA":
		soma = dur[i] * 6.7 + soma
	elif nomes[i] == "ESCALADA":
		soma = dur[i] * 9.7 + soma
	elif nomes[i] == "HIDROGINASTICA":
		soma = dur[i] * 5 + soma
		
	i = i + 1

print(round(soma,2))


