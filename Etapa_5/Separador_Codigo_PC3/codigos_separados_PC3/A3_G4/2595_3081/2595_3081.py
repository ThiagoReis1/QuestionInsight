from numpy import*
vet = array(eval(input("Oscila...: ")))
x = 0
i = 1
z = 0
while(i<len(vet)):
	if(vet[i]<=-vet[0]):
		print(i)
		i = i +1
		z = z + 1
	else:
		i = i + 1
print(z)
