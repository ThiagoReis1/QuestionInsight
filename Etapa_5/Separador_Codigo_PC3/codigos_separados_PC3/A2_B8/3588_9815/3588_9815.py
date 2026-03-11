from numpy import *
v = array(eval(input("Insira o Vetor: ")))

i = 0
total = 10000

while i < size(v):
	if v[i] == 1:
		total *= 2
	elif v[i] == 2:
		total = total
	elif v[i] == 3:
		total /= 2
	elif v[i] == 4:
		total /= 4
	i += 1

print(total)
	