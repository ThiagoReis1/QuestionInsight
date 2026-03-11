valordevenda = float(input("Valor de vendas: "))

porcentagem1 = 5/100
porcentagem2 = 10/100

caso1 = valordevenda * porcentagem1

excedente = valordevenda - 1000
num1 = excedente * porcentagem2

num2 = (valordevenda - excedente) * porcentagem1
soma = (num1 + num2)


if(valordevenda <= 1000):
	print(round(caso1,2))
else:
	
	print(round(soma,2))

	



