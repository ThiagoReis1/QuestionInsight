from numpy import*
vet=input()
a=len(vet)
x=0
b=0
y=0
d=0
c=zeros(a, int)
vet2=""
if((a<11)or(a>11)):
	print("INVALIDO")
else:
	for i in range(a):
		if(i%2!=0):
			vet2=vet2+vet[i]
	print(vet2)