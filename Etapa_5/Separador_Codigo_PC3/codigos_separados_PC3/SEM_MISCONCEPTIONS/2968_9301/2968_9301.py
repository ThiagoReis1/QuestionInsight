lancheousalgado = input("digite L ou S:")
quantidade = int(input("digite a quantidade de lanches ou salgados: "))
quantidade_refris = int(input("digite a quantidade de refris: "))

lanche = 5.00
salgado = 3.50
refrigerante = 4.00

if	lancheousalgado == "L":
	total = (quantidade_refris * refrigerante) + (quantidade * lanche)
	
else:
	total = (quantidade_refris * refrigerante) + (quantidade * salgado)
print(round(total, 2))