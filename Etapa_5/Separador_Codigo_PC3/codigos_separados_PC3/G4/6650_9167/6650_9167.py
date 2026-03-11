from numpy import *
p = array(eval(input("numeros do vetor:  ")))
i = 0
peso = 4
total = 0
while i <len(p):
	total = total + p[i] * peso
	peso = peso - 1
	i = i + 1
s = total/7
print(round(s, 2))
