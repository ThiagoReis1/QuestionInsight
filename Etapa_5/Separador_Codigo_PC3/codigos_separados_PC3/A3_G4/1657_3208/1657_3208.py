from numpy import*
v=input("")
a=v.upper()
d=v.split(',')
az=0
ca=0
fl=0
pa=0
wi=0
vet=zeros(5,dtype=int)
for i in d :
	
	if i=="AZ":
		az=az+1
	elif i=="CA":
		ca=ca+1
	elif i=="FL":
		fl=fl+1
	elif i=="PA":
		pa=pa+1
	else:
		wi=wi+1

vet[0]=az
vet [1]=ca
vet[2]=fl
vet[3]=pa
vet[4]=wi

print(max(vet))
print(vet)
