from numpy import *

v = array(eval(input("Insira as notas: ")))
i = 0
nota = 0
v1 = [3, 5, 1]

while i < size(v):
	nota += v[i] * v1[i]
	i += 1
	
nota = nota/sum(v1)

print(round(nota, 2))