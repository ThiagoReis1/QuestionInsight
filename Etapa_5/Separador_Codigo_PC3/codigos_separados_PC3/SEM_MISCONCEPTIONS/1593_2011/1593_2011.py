from numpy import *

vet = array(eval(input("  ")))

soma = 0
total = 0
for i in range(size(vet)):
	soma= soma + vet[i]*(i+1)
	total = i + 1 + total
	
print(round(soma/total,2))