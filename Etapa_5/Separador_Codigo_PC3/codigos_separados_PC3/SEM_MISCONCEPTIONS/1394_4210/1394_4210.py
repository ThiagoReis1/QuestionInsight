horas = int(input())
salario1 = float(50*horas)
salario2 = float(50*20+70*(horas-20))

if(horas<=20):
	print(round(salario1,2))
else:
	print(round(salario2,2))