#entradas
unidade = input("")
valor = float(input(""))

if unidade.upper() == "K":
	lb = valor * 2.20462
	print(round(lb,2))
else:
	kg = valor / 2.20462
	print(round(kg,2))
