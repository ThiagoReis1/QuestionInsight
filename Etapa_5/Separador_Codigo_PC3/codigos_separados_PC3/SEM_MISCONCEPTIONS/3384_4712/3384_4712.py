unidade = (input("C ou K"))
valor = float(input("valor"))
if(unidade.upper() == "K"):
	conversao = 35.274*valor
else:
	conversao = valor/35.274
print (round(conversao,2))