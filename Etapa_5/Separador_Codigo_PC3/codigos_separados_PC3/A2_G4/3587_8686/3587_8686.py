from numpy import *

n = array(eval(input()))

i = 100.0
cont = 0

while cont < size(n):
	if n[cont] == 1:
		i = i * 5
	if n[cont] == 2:
		i = i * 3
	if n[cont] == 3:
		i = i
	if n[cont] == 4:
		i = i/2
	cont += 1
print(round(i, 2))	