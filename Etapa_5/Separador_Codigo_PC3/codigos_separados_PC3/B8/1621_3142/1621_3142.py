from numpy import*
nomes = array(eval(input("")))
quant = array(eval(input("")))

i = 0
total = 0

while(i < size(nomes)):
	if(nomes[i].upper() == "ARROZ"):
		total = total + quant[i]*1.25
	elif(nomes[i].upper() == "FEIJAO"):
		total = total + quant[i]*2.60
	elif(nomes[i].upper() == "BIS"):
		total = total + quant[i]*1.80
	elif(nomes[i].upper() == "MIOJO"):
		total = total + quant[i]*0.85
	elif(nomes[i].upper() == "FANTA"):
		total = total + quant[i]*3.20
	i = i + 1
print(round(total,2))