horas = int(input("Digite o numero de horas trabalhadas pelo professor: "))

if(horas>0 and horas<=20):
	x = float(horas*50)
	print(round(x, 2))
else:
	hrsadd = (horas - 20) * 70
	result = float(hrsadd + 20*50)
	print(round(result, 2))