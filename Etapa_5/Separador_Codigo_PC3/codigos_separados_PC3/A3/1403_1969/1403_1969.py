#Jogo de RPG.
a = input("Malha ou Placas: ")
b = int(input("Destreza: "))

malha = 15 * 2 - 1
placas = 20 * 2 - 18

if(a == "malha") :
	print(int(malha))

else:
	print(int(placas))