unidade = input("unidade da velocidade :")
valor = float(input("valor da velocidade :"))

if(unidade == "M"):
	V = round(3.6*valor , 2)
else:
	V = round(valor/3.6 , 2)
print(V)