horas = int(input())
if (horas <=20):
	resultado = horas*50
else:
	resultado = (20*50) + ((horas - 20)*70)
print(round(resultado,2))