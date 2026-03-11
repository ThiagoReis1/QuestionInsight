ano = int(input("nascimento: "))
pais = input("B ou R:").upper()
a = 2023 - ano

if pais == "B":
	if a >= 18:
		print("sim")
		print(a - 18)
	else:
		print("nao")
		print(18-a)

elif pais == "R":
	if a >= 21: 
		print("sim")
		print(a - 21)
	else:
		print("nao")
		print(21 - a)
		
else:
	print("invalido")