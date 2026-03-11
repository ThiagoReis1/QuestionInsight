from numpy import*
ARROZ= 1.25
FEIJAO= 2.60
BIS= 1.80
MIOJO= 0.85
FANTA= 3.20
comida=array(eval(input()))
quantidade=array(eval(input()))
preco=0
i=0
while(i<size(comida)):
	if(comida[i]=="ARROZ"):
		preco=preco+(ARROZ*quantidade[i])
		i=i+1
	elif(comida[i]=="FEIJAO"):
		preco=preco+(FEIJAO*quantidade[i])
		i=i+1
	elif(comida[i]=="BIS"):
		preco=preco+(BIS*quantidade[i])
		i=i+1
	elif(comida[i]=="MIOJO"):
		preco=preco+(MIOJO*quantidade[i])
		i=i+1
	else:
		preco=preco+(FANTA*quantidade[i])
		i=i+1
		
print(round(preco,2))
