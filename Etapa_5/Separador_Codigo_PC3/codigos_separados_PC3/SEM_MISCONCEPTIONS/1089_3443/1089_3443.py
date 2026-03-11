valor1= float(input("valor1"))
valor2= float(input("valor2"))
valor3= float(input("valor3"))
limite=float(input("limite"))
total = (valor1+valor2+valor3)
print(round(total,2))
if (total<=limite):
	print("Nao ultrapassou")
else:
	print("Ultrapassou")
