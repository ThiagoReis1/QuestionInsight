from numpy import *
vet_nomes = array(eval(input("Digite os nomes dos produtos: ")))
vet_quant = array(eval(input("Digite a quantidade dos produtos: ")))

i = 0
cont0 = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

while (i < size(vet_nomes)):
	if(vet_nomes[i] == 'ARROZ'):
		cont0 = cont0 + (vet_quant[i]*1.25)
	elif(vet_nomes[i] == 'FEIJAO'):
		cont1 = cont1 + (vet_quant[i]*2.60)
	elif(vet_nomes[i] == 'BIS'):
		cont2 = cont2 + (vet_quant[i]*1.80)
	elif(vet_nomes[i] == 'MIOJO'):
		cont3 = cont3 + (vet_quant[i]*0.85)
	elif(vet_nomes[i] == 'FANTA'):
		cont4 = cont4 + (vet_quant[i]*3.20)
	i = i + 1
	
Total_da_conta = (cont0 + cont1 + cont2 + cont3 + cont4)
print(round(Total_da_conta, 2))