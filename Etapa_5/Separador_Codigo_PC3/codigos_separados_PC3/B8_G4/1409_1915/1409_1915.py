atk = input("tipo de atk:")
var1 = int(input("1: "))
var2 = int(input("2: "))
var3 = int(input("3: "))
var4 = int(input("4:"))

if (atk == "espada"):
	dano = (var1 + 6) + (var2 +6) + (var3 + 6) + (var4 + 6)
	print(dano)
elif (atk == "cauda"):
	dano = (var1 + var2 + var3) * var4
	print(dano)
	