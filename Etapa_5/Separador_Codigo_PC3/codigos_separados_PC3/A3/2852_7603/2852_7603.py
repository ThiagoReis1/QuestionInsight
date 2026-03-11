from numpy import *

num = array(eval(input(" ")))

soma = 0 #variavel acumuladora
total = sum(num)
for i in range(size(num)):
	if num[i] != "88":
		soma = sum(num)
	else:
		soma = (sum(num[i])/2) + sum(num[i,-1]) - 88

print(soma)

