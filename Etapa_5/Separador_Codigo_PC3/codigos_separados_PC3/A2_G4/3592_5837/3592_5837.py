from numpy import*

vet=array(eval(input("Faces do dado: ")))
i=0
p=100
while i<size(vet):
	if vet[i]==1:
		p=p
		i=i+1
	elif vet[i]==2:
		p=p+(2*p) - (p)
		i=i+1
	elif vet[i]==3:
		p=p+(p/3)-p
		i=i+1
	elif vet[i]==4:
		p=p+(p*4)-p
		i=i+1
	elif vet[i]==5:
		p=p+(p/5)-p
		i=i+1
	else:
		p=p+(p*6)-p
		i=i+1
print(round(p,2))