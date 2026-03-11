hora = float(input("Informe as horas trabalhadas: "))
pag = 0

if hora <= 10:
	pag = hora * 50 + 500
elif hora > 10 and hora < 20:
	pag = hora * 60 + 600
elif hora > 20 and hora < 30:
	pag = hora * 70 + 700
else:
	pag = hora * 80 + 800

print(round(pag, 2))