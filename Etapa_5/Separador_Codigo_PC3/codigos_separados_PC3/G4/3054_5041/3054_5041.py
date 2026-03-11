h = float(input("Informe a qunatidade de horas trabalhadas: "))

if h>=0 and h<=10:
	val = 50
	bon = 500
elif h>10 and h<=20:
	val = 60
	bon = 600
elif h>20 and h<=30:
	val = 70
	bon = 700
else:
	val = 80
	bon = 800
pag = h*val + bon
print(round(pag, 2))