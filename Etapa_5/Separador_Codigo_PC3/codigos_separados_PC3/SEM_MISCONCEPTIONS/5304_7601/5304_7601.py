n_bac = int(input("Digite o numero da colonia de bacterias: "))
horas = int(input("Digite o total de horas: "))

t = 0

while t < horas:
	t = t + 1
	n_bac = n_bac + int(n_bac * 0.15)
	print(n_bac)
	