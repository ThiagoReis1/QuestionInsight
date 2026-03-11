from numpy import*
nomes = array(eval(input("nomes do produto: ")))
qtd = array(eval(input("quantidade de cada produto: ")))
elem = size(nomes)
i = 0
preco = 0
while(i < elem):
	if(nomes[i].upper() == "ARROZ"):
		a = qtd[i]
		preco = preco + a*1.25
	elif(nomes[i].upper() == "FEIJAO"):
		a = qtd[i]
		preco = preco + a*2.60
	elif(nomes[i].upper() == "BIS"):
		a = qtd[i]
		preco = preco + a*1.80
	elif(nomes[i].upper() == "MIOJO"):
		a = qtd[i]
		preco = preco + a*0.85
	elif(nomes[i].upper() == "FANTA"):
		a = qtd[i]
		preco = preco + a*3.20
	i = i + 1
print(round(preco,2))
