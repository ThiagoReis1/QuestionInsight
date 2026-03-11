from numpy import *
x = input().split(',')
soma = zeros(len(x), dtype=int)
for i in x:
	if(i == "AZ"):
		soma = soma + 1
	elif(i == "CA"):
		soma = soma[i] + 1
	elif(i == "FL"):
		soma = soma[i] + 1
	elif(i == "PA"):
		soma = soma[i] + 1
	elif(i == "WI"):	
		soma = soma[i] + 1
print(max(soma))
print([soma,soma1,soma2,soma3,soma4])