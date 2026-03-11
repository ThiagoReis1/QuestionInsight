programa = input("Linguagem de programacao: ").upper()
contador = 0 

while programa != "X":
	if programa == "A":
		contador += 1
		programa = input("Linguagem de programcao: ").upper()
	elif programa == "P":
		programa = input("Linguagem de programacao: ").upper()
	elif programa == "C":
		programa = input("Linguagem de programacao: ").upper()
	
print(contador)
