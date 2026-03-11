from numpy import *

# entrada

vet = array(eval(input()))

# acumulador

num = 0 # numerador

# laço 1

for i in range(size(vet)):
	
	num = num + (exp(vet[i]))
	

m = log(num/exp(size(vet)))
print (round(m, 2))