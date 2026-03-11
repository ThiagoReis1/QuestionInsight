c1 = float(input("informe o valor da primeira compra"))
c2 = float(input("informe o valor da segunda compra"))
c3 = float(input("informe o valor da terceira compra"))
limite = float(input("informe o limite do cartao"))
resultado = c1 + c2 + c3
print(round(resultado, 2))
if (resultado > limite):
	print("Ultrapassou")
else:
	print("Nao ultrapassou")
