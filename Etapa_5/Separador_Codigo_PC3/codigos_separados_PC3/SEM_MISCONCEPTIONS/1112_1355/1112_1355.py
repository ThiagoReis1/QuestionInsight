salario = float(input("Digite o salario: "))

if 0< salario <=800:
	salario2=(salario*0.5)+salario
	print("Entrada: R$", salario)
	print("Novo salario: R$",round(salario2,2))
	
elif 800< salario <=1000:
	salario2=(salario*0.4)+salario
	print("Entrada:R$", salario)
	print("Novo salario: R$",round(salario2,2))
elif 1000<salario<=1200:
	salario2=(salario*0.3)+salario
	print("Entrada:R$", salario)
	print("Novo salario: R$",round(salario2,2))
elif 1200<salario<=1400:
	salario2=(salario*0.2)+salario
	print("Novo salario: R$",round(salario2,2))
	print("Entrada:R$", salario)
elif 1400<salario<=1600:
	salario2=(salario*0.1)+salario	
	print("Novo salario: R$",round(salario2,2))
	print("Entrada:R$", salario)
elif salario>1600:
	salario2=(salario*0.05)+salario
	print("Novo salario: R$",round(salario2,2))
	print("Entrada:R$", salario)	
else:
	print("Entrada:R$", salario)	
	print("Dado invalido")
			
	