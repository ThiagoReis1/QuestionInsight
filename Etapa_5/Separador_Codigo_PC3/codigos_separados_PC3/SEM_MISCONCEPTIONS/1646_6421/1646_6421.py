from numpy import *
vet = array(eval(input(":")))
f = 0
lista = []
				
for i in range(len(vet)):
	if (vet[i] <= 50):
		f = f + 1
		lista.append(i)		
				
print(f)
print(array(lista))				