from numpy import*
#vou criar um vetor
#o elemento zero desse vator vai ser o parametro para comparar (é o limite)
vet=array(eval(input("valores de limite esperado e nivel de acidente:  ")))
k = 0#minha contadora de padrao de acidentes
j=0 #contadora de enfeita para nao me perder
for i in range(size(vet)):
	if(vet[i]<vet[0]):
		print(i)
		k = k +1
	else:
		j = j + 1
print(k)
