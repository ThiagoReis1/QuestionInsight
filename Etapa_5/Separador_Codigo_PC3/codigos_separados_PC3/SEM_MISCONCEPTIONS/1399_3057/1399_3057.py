candidato1 = float (input ("total de votos do candidato a.r: "))
candidato2 = float (input ("total de votos do candidato d.o: "))
soma = candidato1 + candidato2

if	(candidato1 > candidato2):
	x = (candidato1 / soma) * 100
	print ("Ambrosio Rutra", round (x , 2))

if	(candidato2 > candidato1):
	y = (candidato2 / soma) * 100
	print ("Demelza Olecram", round (y , 2))

