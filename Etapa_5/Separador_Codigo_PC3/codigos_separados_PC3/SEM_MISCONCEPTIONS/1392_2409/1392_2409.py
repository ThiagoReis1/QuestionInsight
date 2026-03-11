consumo = int(input("digite o consumo de agua: "))
taxa = 30

if(consumo < 10):
	cobranca = 3*consumo
else:
	cobranca = 3.5*consumo

conta = taxa + cobranca 

print(round(conta, 2))