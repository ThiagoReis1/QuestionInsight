# Incertables

wpn = input("Weapon of choice: ")
dex = int(input("Destreza do jogador: "))
d10 = int(input("Result of first d10: "))
d102 = int(input("Result of second d10: "))

# Computables
if( (d10 > 10) or (d102 > 10) or ((d10 > 10) and (d102 > 10))):
	print("Entrada invalida")
elif((wpn == "CIMITARRA")):
	print(2*(d10 + d102) + 2*dex)
elif(wpn == "KATANA"):
	print(2*(d10 + d102) + dex)
elif(wpn == "SABRE"):
	print(d10 + d102 + 2*dex)