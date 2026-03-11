from numpy import *
vet = array(eval(input("Digite as frequencias: ")))
cont=0
for i in vet:
	if(i>=70):
		cont = cont +1
n=zeros(cont, dtype=int)
nova_cont=0
for i in range(size(vet)):
	if(vet[i] >= 70):
		n[nova_cont]=i
		nova_cont= nova_cont + 1
print(cont)
print(n)