from numpy import *


x = 0
j = 0

vet = array(eval(input("Digite os valores de saque: ")))


for i in range (size(vet)):
	if(vet[i] <= 50):
		x = x + 1
cont = zeros(x, dtype=int)
for i in range (size(vet)):
	if(vet[i] <= 50):
		cont[j] = i
		j = j + 1
print(x)
print(cont)
	