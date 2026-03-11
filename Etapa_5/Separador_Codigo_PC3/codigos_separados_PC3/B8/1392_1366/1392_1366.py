consumo = float(input())
valor = 30.0

if consumo < 10 and consumo > 0:
	valor += consumo * 3
elif consumo >= 10:
	valor += consumo * 3.5 
	
print(round(valor, 2))