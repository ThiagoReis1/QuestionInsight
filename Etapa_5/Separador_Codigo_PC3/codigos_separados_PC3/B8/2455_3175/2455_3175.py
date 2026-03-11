nivel = int(input("qual o nivel: "))
horas = int(input("qual a quantidade de horas: "))

valor1 = 12
valor2 = 17
valor3= 25

if(nivel==1):
	salario = (horas*valor1)
	print(round(salario, 2))
elif(nivel==2):
	salario = (horas*valor2)
	print(round(salario, 2))
elif(nivel==3):
	salario = (horas*valor3)
	print(round(salario, 2))