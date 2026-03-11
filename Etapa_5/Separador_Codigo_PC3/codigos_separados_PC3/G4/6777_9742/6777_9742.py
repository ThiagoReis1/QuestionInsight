a = int(input("Ano:"))
p = input("B ou I:").upper()



if p=="B":
	d = 2023-a
	if d>=18:
		print("sim")
		print(d-18)
	else:
		print("nao")
		print(18-d)
elif p=="I":
	d = 2023-a
	if d>=17:
		print("sim")
		print(d-17)
	else:
		print("nao")
		print(17-d)
else:
	print("invalido")