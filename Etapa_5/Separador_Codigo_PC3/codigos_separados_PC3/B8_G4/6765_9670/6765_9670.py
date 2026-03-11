ano= int(input("ano referente ao nascimento: ")) 
pais= input("B para Brasil, R para Russia: ").upper()

apt= 2023 - ano

if pais != "B" and pais != "R":
	print("invalido")
elif pais == "B" and apt>= 18:
	print("sim")
	print(apt - 18)
elif pais == "R" and apt >=21:
	print("sim")
	print(apt - 21)
elif pais == "B" and apt <18:
	print("nao")
	print(18 - apt)
elif pais == "R" and apt <= 21:
	print("nao")
	print(21 - apt)

		







