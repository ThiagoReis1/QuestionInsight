from numpy import*
vet = array(eval(input("Digite a quantidade de turmas: ")))

cont=0
for x in vet:
	if x%2==0:
		cont=cont+1
		
vet2 = zeros(cont, dtype=int)

j = 0
for i in range(size(vet)):
	if vet[i]%2==0:
		vet2[j]=i
		j=j+1
print(cont)
print(vet2)