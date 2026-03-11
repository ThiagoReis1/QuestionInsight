from numpy import*
var1=input('insira:').upper().split(',')
prod= zeros(4,dtype=int)

for i in var1:
	if i == 'E':
	prod[0] += 1
	elif i == 'V':
		prod[1] += 1
	elif i == 'A':
		prod[2] += 1
	elif i == 'D':
		prod[3] += 1
		
print(prod)