dat = int(input("data: "))
pais = input("pais: ").upper()
t = 2023 - dat

if pais == 'E':
	if t >= 16:
		print("sim")
		print(t-16)
	else:
		print("nao")
		print(16-t)
elif pais == 'B':
	if t >= 18:
		print("sim")
		print(t-18)
	else:
		print("nao")
		print(18-t)
else:
	print("invalido")