from numpy import*
vet=input("quantidade de pessoas: ").upper().split(',')
cont=zeros(5, dtype=int)
for i in range(size(vet)):
	if(vet[0]=='AZ'):
		cont=cont+1
	elif(vet[1]=='CA'):
		cont=cont+1
	elif(vet[2]=='FL'):
		cont=cont+1
	elif(vet=='PA'):
		cont=cont+1
	elif(vet[4]=='WI'):
		cont=cont+1

	print(max(vet)
	print(cont)
	