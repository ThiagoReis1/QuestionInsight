from math import factorial as fct

x = float(input())
k = int(input())
e = 0
cont = 0

while cont < k:
	e += pow(x, cont) / fct(cont)
	cont += 1

print(round(e, 9))