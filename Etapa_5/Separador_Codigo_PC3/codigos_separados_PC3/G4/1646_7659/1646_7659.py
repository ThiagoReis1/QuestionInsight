from numpy import *

saques = array(eval(input("digite os valores dos saques:")))

soma = 0

for i in range(len(saques)):
	if saques[i] <= 50 :
		soma = soma  + 1

a = zeros(soma, dtype=int)
j = 0
for i in range(len(saques)):
	if saques[i] <= 50:
		a[j] = i
		j = j + 1
		
print(soma)
print(a)