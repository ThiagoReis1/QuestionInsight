resposta= input().upper()

quant=0

while resposta != "S":
	if resposta== "SIM":
		quant+= 1 
	resposta= input().upper()
print(quant)