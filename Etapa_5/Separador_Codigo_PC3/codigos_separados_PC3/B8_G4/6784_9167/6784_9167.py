a = int(input("data de nascimento: "))
b = input("em q pais nasceu; ").upper()

c = 2023-a
if b=="B" and c>=21:
	print("sim")
	print(c-21)
elif b=="B" and c<21:
	print("nao")
	print(a-2023+21)
elif b=="R" and c>=18:
	print("sim")
	print(c-18)
elif b=="R" and c<18:
	print("nao")
	print(a-2023+18)
elif not b=="B" or b=="R":
	print("invalido")