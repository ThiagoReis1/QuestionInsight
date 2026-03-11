from numpy import*

f = input("").split(',')

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0



for i in range(0,len(f)):
	if(f[i] == "AC"):
		cont1 = cont1 + 1
	elif(f[i] == "AM"):
		cont2 = cont2 +1
	elif(f[i]== "PA"):
		cont3 = cont3 + 1
	elif(f[i]== "RO"):
		cont4 = cont4 + 1
	elif(f[i]== "RR"):
		cont5 = cont5 + 1
vet = zeros(5,dtype=int)
vet[0] = cont1
vet[1] = cont2
vet[2] = cont3
vet[3] = cont4
vet[4] = cont5

print(max(vet))
print(vet)	

















