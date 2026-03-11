from numpy import*
vet = array(eval(input("")))
quant_via = 0
for i in range(size(vet)):
	if(vet[0]>vet[i]):
		quant_via+=1
		print(i)
print(quant_via)