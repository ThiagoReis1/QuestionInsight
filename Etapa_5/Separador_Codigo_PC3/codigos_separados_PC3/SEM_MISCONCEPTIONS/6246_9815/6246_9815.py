result = input("Insira A para vitoria do time A, insira B para vitoria do time B, insira E para empate: ").upper()
vitA = 0

while result != "X":
	if result == "A":
		vitA += 1
		result = input("Insira Proximo Resultado: ")
	else:
		vitA += 0
		result = input("Insira Proximo Resultado: ")

print(vitA)