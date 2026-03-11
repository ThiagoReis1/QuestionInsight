votos = int(input("Qual a quantidade de votos para Ambrosio Rutra: "))
votos1= int(input("Qual a quantidade de votos para Demelza Olecram: "))
total = votos + votos1
if (votos > votos1):
	print("Ambrosio Rutra")
	print(float(round((votos)*100/total, 2)))
else: 
	print("Demelza Olecram")
	print(float(round((votos1)*100/total, 2)))