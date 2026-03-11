x = int(input("ano de nascimento: "))
y = input("pais: ").upper()

i = 2023 - x

if y == "B":
	if i >= 21:
		print("sim")
		print(i - 21)
	else:
		print("nao")
		print(21 - i)
elif y == "R":
	if i >= 18:
		print ("sim")
		print(i - 18)
	else:
		print ("nao")
		print(18 -  i)
else:
	print("invalido")
		