valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
limite = float(input())
total = valor1 + valor2 + valor3 + valor4
if total <= limite:
	print(round(total,2),"Sim")
else:
	print(round(total,2),"Nao")