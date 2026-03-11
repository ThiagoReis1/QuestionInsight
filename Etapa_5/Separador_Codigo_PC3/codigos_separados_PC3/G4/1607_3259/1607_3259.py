from numpy import *
vet = array(eval(input("Paradas: ")))

i = 0
s = 0
k = 1

while(i<size(vet)):
	d = (vet[k] - vet[k-1]) * 3 
	s = s + d
	i = i + 1
	k = k+1	
print(d)