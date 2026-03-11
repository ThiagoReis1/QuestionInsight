from numpy import*
vet = array(eval(input("")))

p = 0 
for i in range(size(vet)):
	if vet[i] == 1:
		p = p + 80
	elif vet[i] == 2:
		p = p + 40
	elif vet[i] == 3:
		p = p +20
	elif vet[i] == 4:
		p = p + 10
print(p)
