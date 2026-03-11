qtde = float(input("escreva a quantidade de macas: "))
sdes = 0.30
cdes = 0.25
if qtde < 12:
	valor = qtde*sdes
	print(round(valor, 2))
else:
	valor = qtde*cdes
	print(round(valor, 2))