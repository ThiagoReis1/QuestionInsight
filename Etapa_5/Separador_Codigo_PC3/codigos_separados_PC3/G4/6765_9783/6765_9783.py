naci = int(input(": "))
pair = input(": ").upper()
dog =  2023 - naci
if pair == "B":
	if dog == 18:
		print("sim")
		print( 18 - dog)
	else:
		print("nao")
		print(18 - dog)
elif pair == "R":
	if dog == 21:
		print("sim")
		print(21 - dog)
	else:
		print("nao")
		print(21 - dog)
else:
	print("invalido")