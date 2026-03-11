from numpy import *
vet = array(input(":"))
vet1 = array(eval(input(":")))
x = 0
s = (5 * ((vet[x]) * (vet1[x] / 100))

soma = 0
while(x < size(vet)):
	x = x + 1
	soma = soma + s
	print(round(soma,2))

