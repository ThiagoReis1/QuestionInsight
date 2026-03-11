result = input("resultado jogo: ").upper()
cont = 0
while result != "X":
	if result == "A":
		cont += 1
	result = input("resultado joso: ").upper()
print(cont)