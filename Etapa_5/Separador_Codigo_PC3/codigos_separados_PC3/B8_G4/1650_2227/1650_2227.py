from numpy import*
vet=input("letras ").split(',')

cont=zeros(5,dtype=int)

for i in vet:
	if i.upper()=="P":
		cont[0]+=1
	elif i.upper()=="C":
		cont[1]+=1
	elif i.upper()=="R":
		cont[2]+=1
	elif i.upper()=="L":
		cont[3]+=1
	elif i.upper()=="B":
		cont[4]+=1
print(max(cont))
print(cont)
	
			
	