a=int(input("Quando oce nasceu: "))
p=input("Digite B para Brasil ou R para Russia: ").upper()
i=2023-a

if p == "B":
	if i >= 18:
		f=18-i
		print("sim")
		print(f)
	else:
		f=18-i
		print("nao")
		print(f)
elif p=="R":
	if i>=21:
		f=21-i
		print("sim")
		print(f)
	else:
		f=21-i
		print("nao")
		print(f)
else:
	print("invalido")


