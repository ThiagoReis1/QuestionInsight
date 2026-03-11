consumo = float(input("digite o total consumido: "))
taxa = 30.0

f1 = (taxa + (3 * consumo))        # - de 10 metros
f2 = (taxa + (3.5 * consumo))      # + de 10 m

if(consumo < 10):
	valor = f1
	
else:
	consumo > 10
	valor = f2
	
print(round(valor, 2))
	