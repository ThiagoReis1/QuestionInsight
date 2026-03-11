valor_compra = float(input("valor: "))
valor_compra2 = float(input("valor2: "))
valor_compra3 = float(input("valor3: "))
limite = float(input("limite: "))

x = valor_compra + valor_compra2 + valor_compra3

if round(x,2) > limite:
	msg = "Ultrapassou"
else:
	msg = "Nao ultrapassou"
print(round(x,2))
print(msg)