u = input("R para radianos ou G para graus: ").upper()
ang = float(input("Valor do angulo: "))

gr = ang / 0.0174533
ra = 0.0174533 * ang


if (u=="G"):  #aqui ok
	print(round(ra,2))
else:         #trabalhar aqui
	print(round(gr,2))