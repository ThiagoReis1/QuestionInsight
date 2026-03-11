cdg = input("101/102: ")
sal = float(input("salario atual: "))

if (cdg == '101'):
	x = sal + (sal*10/100)
	x1 = "Aumento de 10 por cento"
else: 
	x = sal + (sal*30/100)
	x1 = "Aumento de 30 por cento"
print(round(x, 2))
print(x1)

