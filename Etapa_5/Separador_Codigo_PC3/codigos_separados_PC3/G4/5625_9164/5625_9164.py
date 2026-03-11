prod = input("Qual o produto? T para tapioca e S para salgado: ").upper()
qtd = int(input("Qual a quantidade? "))
qtdacai = int(input("Quantidade de acai: "))
T = qtd * 5.50
S = qtd * 4.00
acai = qtdacai * 10.00

if prod == "T":
	preco = T + acai
	
else:
	preco = S + acai
	
print(round(preco, 2))