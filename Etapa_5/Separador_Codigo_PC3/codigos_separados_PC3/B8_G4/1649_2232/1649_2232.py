from numpy import*

vet=input("").split(',')
cont=zeros(5, dtype=int)

for i in vet:
	if i.upper()=="P":
		cont[0]+=1
	elif i.upper()=="C":
		cont[1]+=1
	elif i.upper()=="M":
		cont[2]+=1
	elif i.upper()=="V":
		cont[3]+=1
	elif i.upper()=="A":
		cont[4]+=1
print(max(cont))
print(cont)