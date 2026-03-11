candidato1 = int(input(""))
candidato2 = int(input(""))
if(candidato1 > candidato2):
	a = (candidato1/(candidato1 + candidato2))*100.0
	print("Ambrosio Rutra")
	print(round(a,2))
else:
	b = (candidato2/(candidato1 + candidato2))*100.0
	print("Demelza Olecram")
	print(round(b,2))