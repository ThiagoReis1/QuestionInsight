salario = float(input(""))

print("Entrada: R$",salario)

if (salario < 0):
	print("Dado invalido")
elif (salario > 0) and (salario <= 800):
	salario = salario + (salario*50/100)
	print("Novo salario: R$",round(salario,2))
elif (salario > 800) and (salario <= 1000):
	salario = salario + (salario*40/100)
	print("Novo salario: R$",round(salario,2))
elif (salario > 1000) and (salario <= 1200):
	salario= salario + (salario*30/100)
	print("Novo salario: R$",round(salario,2))
elif (salario > 1200) and (salario <= 1400):
	salario = salario + (salario*20/100)
	print("Novo salario: R$",round(salario,2))
elif (salario > 1400) and (salario <=1600):
	salario = salario + (salario*10/100)
	print("Novo salario: R$",round(salario,2))
elif (salario > 1600):
	salario = salario + (salario*5/100)
	print("Novo salario: R$",round(salario,2))
else:
	print("Dado invalido")