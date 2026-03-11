from numpy import *

vet1 = input()

i = 0
preco = 0
q_a = 0
q_l = 0
q_p = 0

while i < len(vet1):
	if vet1[i] == 'A':
		preco = preco + 16.75  
		q_a += 1
	elif vet1[i] == 'L':
		preco = preco + 4.60 
		q_l += 1 
	elif vet1[i] == 'P':
		preco = preco + 2.85 
		q_p += 1
	i += 1
print(round(preco, 2), q_a,q_l,q_p)
	