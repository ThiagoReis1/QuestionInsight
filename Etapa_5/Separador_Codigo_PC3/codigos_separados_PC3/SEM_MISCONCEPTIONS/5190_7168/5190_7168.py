cod = input("Qual o seu codigo: ")
salario = float(input("Qual o seu salario: "))

if(cod == "101"):
	chunin = salario * 0.1 + salario
	print(round(chunin, 2))
	print("Aumento de 10 por cento")
else:

	jounin = salario * 0.3 + salario
	print(round(jounin, 2))
	print("Aumento de 30 por cento")
	