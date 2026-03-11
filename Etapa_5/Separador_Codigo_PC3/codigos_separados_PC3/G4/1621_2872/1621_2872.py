from numpy import*
prod = array(eval(input("Digite o nome dos produtos: ")))
quant = array(eval(input("Informe a quantidade: ")))
i = 0
t = 0
while (i<size(prod)):
	if (prod[i]=="ARROZ"):
		t = t + quant[i]*1.25
	if (prod[i]=="FEIJAO"):
		t = t + quant[i]*2.60
	if (prod[i]=="BIS"):
		t = t + quant[i]*1.80
	if (prod[i]=="MIOJO"):
		t = t + quant[i]*0.85
	if (prod[i]=="FANTA"):
		t = t + quant[i]*3.20
	i = i+1
print(round(t,2))