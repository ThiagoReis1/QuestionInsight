limite = float(input("limite do cartao: "))
valor1 = float(input("valor da compra: "))
valor2 = float(input("valor da compra: "))
valor3 = float(input("valor da compra: "))
valor4 = float(input("valor da compra: "))
total = (valor1 + valor2 + valor3 + valor4)
print(round(total, 2))
if(total <= limite):
	msg = "Dentro do limite"
else:
	msg = "Estourou o limite"
print(msg)