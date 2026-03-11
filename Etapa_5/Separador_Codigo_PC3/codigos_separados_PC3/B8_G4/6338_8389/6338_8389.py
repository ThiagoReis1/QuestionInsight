from numpy import*
vet  = array(eval(input("")))
n = int(input(""))
cont = 0
i = 0
while(i < size(vet)):
	
	if(vet[i] > n ):
		cont = cont + 1
	elif(vet[i]== n):
		print(i)
	i = i + 1
print(cont)