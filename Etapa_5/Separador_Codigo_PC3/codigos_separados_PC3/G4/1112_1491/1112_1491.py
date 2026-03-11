s = float(input("Insira o salario: "))
print("Entrada: R$", s)

if(s < 0):
	print("Dado invalido")
elif (s > 0) and (s <= 800):
	y = s + (s * 0.5)
	print("Novo salario: R$", round(y ,2))
elif(s > 800) and (s <= 1000):
	y = s + (s * 0.4)
	print("Novo salario: R$", round(y ,2))
elif(s > 1000) and (s <= 1200):
	y = s + (s * 0.3)
	print("Novo salario: R$", round(y ,2))
elif(s > 1200) and (s <= 1400):
	y = s + (s * 0.2)
	print("Novo salario: R$", round(y ,2))
elif(s > 1400) and (s <= 1600):
	y = s + (s * 0.1)
	print("Novo salario: R$", round(y ,2))
else:
	y = s + (s * 0.05)
	print("Novo salario: R$", round(y ,2))