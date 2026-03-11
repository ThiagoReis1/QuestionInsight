cd=int(input("codigo: "))
sa=float(input("salario atual: "))

if(cd==101):
	sa=sa+(sa*0.1)
	print(round(sa, 2))
	print("Aumento de 10 por cento")
else:
	if(cd==102):
		sa=sa+(sa*0.3)
		print(round(sa, 2))
		print("Aumento de 30 por cento")
