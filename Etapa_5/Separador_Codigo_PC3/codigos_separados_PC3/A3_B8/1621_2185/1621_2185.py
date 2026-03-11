from numpy import *

produtos = array(eval(input("produtos:")))
quantidade = array(eval(input("quantidades: ")))
i = 0
cont0 = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0

while i < size(quantidade):
	if(produtos[i] == "ARROZ"):
		cont0 = cont0 + (quantidade[i] * 1.25)
	elif(produtos[i] == "FEIJAO"):
		cont1 = cont1 + (quantidade[i] * 2.60)
	elif(produtos[i] == "BIS"):
		cont2 = cont2 + (quantidade[i] * 1.80)
	elif(produtos[i] == "MIOJO"):
		cont3 = cont3 + (quantidade[i] * 0.85)
	elif(produtos[i] == "FANTA"):
		cont4 = cont4 + (quantidade[i] * 3.20)
	i = i + 1
		
total = (cont0 + cont1 + cont2 +cont3 + cont4)
print(round(total, 2))
			
	