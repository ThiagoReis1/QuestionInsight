from numpy import*

cor=input("cor: ").split(',')

vet=zeros(5,dtype=int)

for i in cor:
	if(i == "P"):
		vet[0] += 1
	elif(i == "C"):
		vet[1] += 1
	elif(i == "R"):
		vet[2] += 1
	elif(i == "L"):
		vet[3] += 1
	elif(i == "B"):
		vet[4] += 1
print(max(vet))
print(vet)