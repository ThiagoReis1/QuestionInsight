A = int(input('quantidade de votos do candidato A :'))
B = int(input('quantidade de votos do candidato B :'))

sm_v = (A + B)

candidatoA = ((A * 100) / sm_v)
candidatoB = ((B * 100) / sm_v)

if ( candidatoA > candidatoB):
	
	print("Ambrosio Rutra")
	print(round(candidatoA, 2))
else :
	print("Demelza Olecram")
	print(round(candidatoB, 2))