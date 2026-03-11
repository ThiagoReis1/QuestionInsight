valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
limite = float(input())

total = valor1+valor2+valor3
print(round(total,2))

if(total<=limite):
	print("Nao ultrapassou")
else:
	print("Ultrapassou")

