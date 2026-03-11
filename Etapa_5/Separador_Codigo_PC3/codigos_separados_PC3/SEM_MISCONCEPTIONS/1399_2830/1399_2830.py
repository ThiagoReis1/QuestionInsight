votos_a = int(input())
votos_d = int(input())

total = votos_a + votos_d

if (votos_a > votos_d):
	print("Ambrosio Rutra")
	print(round((votos_a/total*100),2))
else:
	print("Demelza Olecram")
	print(round((votos_d/total*100),2))
