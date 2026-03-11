horas = int(input("horas trabalhadas: "))

if horas>=0 and horas <=10:
	pag = horas * 50.00 + 500.00
elif horas >10 and horas <=20:
	pag = horas * 60.00 + 600.00
elif horas>20 and horas <=30:
	pag = horas * 70.00 + 700.00
elif horas>30:
	pag = horas * 80.00 + 800.00
	
print(round(pag,2))