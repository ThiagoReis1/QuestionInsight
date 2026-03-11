from numpy import*
vet = array(eval(input("notas do aluno")))
cont = 0 
for i in range(size(vet)):
	if(vet[i])%3==0:
		cont = cont + 1 
print(cont)

vet2=zeros(cont,dtype=int)

x=0

for i in range(size(vet)):
	if (vet[i]%3==0):
		vet2[x] = i
		x= x+ 1
print(vet2)