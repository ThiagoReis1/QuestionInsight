from numpy import *
vet = array(eval(input("Vetor de danos: ")))

i = 0
dn = 0
pes = 0 

while(i < size(vet)):
	pes = pes + 1
	dn = dn + vet[i]*pes
	i = i + 1
	
print(dn)