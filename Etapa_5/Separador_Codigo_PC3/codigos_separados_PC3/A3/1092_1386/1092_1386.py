valor1 = float(input("primeira compra?"))
valor2 = float(input("segunda compra?"))
valor3 = float(input("terceira compra?"))
limiteDoCartao = float(input("limite?"))
valortotal = valor1 + valor2 + valor3
print("%0.2f"%valortotal)
if ("valortotal <= limiteDoCartao") :
	print("sim")
else:
	print("nao")