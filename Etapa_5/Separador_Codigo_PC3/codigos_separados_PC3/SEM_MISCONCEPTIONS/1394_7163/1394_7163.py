horaprof = float(input("Quantidade de horas : "))
aula1 = horaprof * 50
aula2 = 20 * 50 + ((horaprof * 70) - (20 * 70))

if horaprof < 20:
	print(round(aula1,2))
else:

	print(round(aula2,2))