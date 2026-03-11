horas = float(input("Horas de trabalho:"))

if(horas<=20):
	salario = 50*horas
else:
	salario = 50*20+(70*(horas-20))

print(round(salario,2))