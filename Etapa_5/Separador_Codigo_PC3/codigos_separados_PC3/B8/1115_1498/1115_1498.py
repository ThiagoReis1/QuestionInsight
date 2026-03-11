salario = float(input("digite o salario atual: "))
codigo = int(input("digite o codigo: "))
print("Entradas: ", salario, "e codigo ", codigo)
if(codigo == 101):
	salarionovo = salario + (salario * 0.8)
	salarionovo = (round(salarionovo, 2))
elif(codigo == 102):
	salarionovo = salario + (salario * 0.65)
	salarionovo = (round(salarionovo, 2))
elif(codigo == 103):
	salarionovo = salario + (salario * 0.6)
	salarionovo = (round(salarionovo, 2))
elif(codigo == 104):
	salarionovo = salario + (salario * 0.55)
	salarionovo = (round(salarionovo, 2))
print("Novo salario: R$", salarionovo)