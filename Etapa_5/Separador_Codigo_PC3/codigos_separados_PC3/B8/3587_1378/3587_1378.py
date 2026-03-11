from numpy import *

vet = array(eval(input()))

i = 0
total = 100
while i < size(vet):
	if vet[i] == 1:
		total *= 5
	elif vet[i] == 2:
		total *= 3
	elif vet[i] == 4:
		total /= 2
	i += 1
print(round(total,2))