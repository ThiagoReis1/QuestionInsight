from numpy import*

vet = array(eval(input("valores")))

i = 0
p = 100

while( i < size(vet)):
	if vet[i] == 1:
		i = i 
		p = p*5
	elif vet[i] == 2:
		i = i  
		p = p*3 
	elif vet[i] == 3:
		i = i  
		p = p
	elif vet[i] == 4:
		i = i 
		p =p/2
	i = i + 1
print(p)