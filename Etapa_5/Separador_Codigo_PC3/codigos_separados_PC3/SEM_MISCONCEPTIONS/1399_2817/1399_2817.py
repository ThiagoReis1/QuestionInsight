voto1 = int(input(""))
voto2 = int(input(""))

candidato1 = "Ambrosio Rutra"
candidato2 = "Demelza Olecram"

if(voto1 > voto2):
	print(candidato1)
	porc = (voto1/(voto1+voto2))*100
	print(round(porc, 2))
else:
	print(candidato2)
	porc = (voto2/(voto1+voto2))*100
	print(round(porc, 2))