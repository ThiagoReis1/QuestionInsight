from numpy import *

string = input("Digite a string: ").split(",")

zero = zeros(4, dtype=int)
tam = len(string)
u = 0
for i in range(tam):
	if string[i] == 'O':
		zero[0] += 1
	elif string[i] == 'D':
		zero[1] += 1
	elif string[i] == 'N':
		zero[2] += 1
	elif string[i] == 'C':
		zero[3] += 1
	
print(zero)