from numpy import *

pontos = array(eval(input("")))

i = 0
total = 10000

while i < size(pontos):
	
	if pontos[i] == 1:
		total = total * 2
	elif pontos[i] == 2:
		total = total 
	elif pontos[i] == 3:
		total = total / 2
	elif pontos[i] == 4:
		total = total/ 4
	i = i + 1

print(round(total, 2))