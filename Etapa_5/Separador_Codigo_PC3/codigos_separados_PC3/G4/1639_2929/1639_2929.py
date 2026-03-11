from numpy import*
cont = 0
vet1=0
vet= array(eval(input("vetor: ")))
for i in vet:
	if(i %2 ==0):
		cont=cont+1
veto= zeros(cont,dtype=int)

for i in range(size(vet)):
	if(vet[i]%2==0):
		veto[vet1]=i
		vet1=vet1 +1
print(cont)
print(veto)