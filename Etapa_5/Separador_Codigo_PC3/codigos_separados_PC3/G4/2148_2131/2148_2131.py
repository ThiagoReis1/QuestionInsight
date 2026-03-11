from numpy import*

vet=array(eval(input("medidas de um poligono: ")))

print(sum(vet))
soma=0
for i in range (size(vet)):
	if(vet[i]>=5):
		soma=soma+1
print(soma)
	