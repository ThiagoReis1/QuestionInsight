# Entradas
valor1= float(input("compra 1: "))
valor2= float(input("compra 2: "))
valor3= float(input("compra 3: "))

limite= float(input())

valor_total = float(valor1+valor2+valor3)

print(round(valor_total, 2))
#condição
if (valor_total<=limite):
	print("Nao ultrapassou")
else:
	print("Ultrapassou")

