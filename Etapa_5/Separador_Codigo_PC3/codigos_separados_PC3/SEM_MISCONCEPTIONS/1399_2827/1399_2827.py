v1 = float(input("Quantidade de votos para o candidato Ambrósio Rutra: "))
v2 = float(input("Quantidade de votos para a candidata Demelza Olecram: "))

total = v1 + v2

if ( v1 > v2):
	print("Ambrosio Rutra")
	print(round(( (v1 * 100) / total ), 2))

else:
	print("Demelza Olecram")
	print(round(( (v2 * 100) / total ), 2))