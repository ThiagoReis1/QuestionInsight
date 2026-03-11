# Entrada 

codigo = int(input("Digite o codigo do cargo:"))
salario = float(input("Digite o salario:"))

# Condicao

if codigo == 101:
	print(round(salario + (salario * (10/100)),2))
	print("Aumento de 10 por cento")
else: 
	print(round(salario + (salario *(30/100)),2))
	print("Aumento de 30 por cento")