from numpy import*
produto = array(eval(input("insira o vetor de nomes")))
q = array(eval(input("insira o vetor de preços")))
i = 0
x =0
while(i < size(produto)):
	if(produto[i] == "ARROZ"):
		x = x + (1.25 * q[i])
	if(produto[i] == "FEIJAO"):
		x = x + (2.60 * q[i])
	if(produto[i] == "BIS"):
		x = x + (1.80 * q[i])
	if(produto[i] == "MIOJO"):
		x = x + (0.85 * q[i])
	if(produto[i] == "FANTA"):
		x = x + (3.20 * q[i])
	i = i +1
print(round(x,2))
		
