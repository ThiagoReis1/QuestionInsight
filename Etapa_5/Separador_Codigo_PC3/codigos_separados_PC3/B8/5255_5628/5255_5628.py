peso = float(input('Peso: '))
distancia = float(input('Distancia: '))
codigo = int(input('Codigo: '))




if codigo == 1:
	roraima = 17.0
	kg = 25
	km = .10
	total = ((peso * kg + distancia * km)*(1.0 + roraima/100))
	print(round(total,2))

elif codigo == 2:
	rondonia = 17.5
	kg = 25
	km = .10
	total = ((peso * kg + distancia * km) * (1.0 + rondonia/100))
	print(round(total,2))

elif codigo == 3:
	amazonas = 18.0
	kg = 25
	km = .10
	total = ((peso*kg + distancia*km) * (1.0 + amazonas/100))
	print(round(total,2))

elif codigo == 4:
	rio = 20.0
	kg = 25
	km = .10
	total = ((peso*kg + distancia*km) * (1.0 + rio/100))
	print(round(total,2))