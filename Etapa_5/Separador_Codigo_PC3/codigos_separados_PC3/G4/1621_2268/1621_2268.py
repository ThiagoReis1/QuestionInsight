from numpy import*
v1 = array(eval(input("digite os nomes de produtos: ")))
v2 = array(eval(input("digite a quantidade: ")))
i = 0
custo = 0
while(i < size(v1)):
	if(v1[i].lower() == "arroz"):
		custo = custo + (v2[i] * 1.25)
	elif(v1[i].lower() == "feijao"):
		custo = custo + (v2[i] * 2.6)
	elif(v1[i].lower() == "bis"):
		custo = custo + (v2[i] * 1.8)
	elif(v1[i].lower() == "miojo"):
		custo = custo + (v2[i] * 0.85)
	else:
		custo = custo + (v2[i] * 3.2)
	i = i + 1
print(custo)


