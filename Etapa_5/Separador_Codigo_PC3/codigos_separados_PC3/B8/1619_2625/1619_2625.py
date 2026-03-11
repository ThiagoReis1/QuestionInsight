from numpy import*

v1 = array(eval(input("")))
v2 = array(eval(input("")))

i = 0
pagamento = 0
while(i<len(v1)):
	if(v2[i]=="QUENTE"):
		potencia = v1[i]*90
		preco = 0.005*potencia
	elif(v2[i]=="MORNO"):
		potencia = v1[i]*45
		preco = 0.005*potencia
	elif(v2[i]=="FRIO"):
		potencia = v1[i]*0
		preco = 0.005*potencia
	pagamento = pagamento + preco
	i = i + 1
print(round(pagamento,2))
	
		
	