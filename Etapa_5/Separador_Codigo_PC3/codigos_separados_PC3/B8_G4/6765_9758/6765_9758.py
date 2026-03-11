n = int(input("nascimento:"))
p = input("B ou R:").upper()

if p == "B":
	if 2023-n >=18:
		print("sim")
		print(2023%n-18)
	else:
		print("nao")
		print()
elif p == "R":
	if 2023-n >=21:
		print("sim")
		print(2023%n-18)
	else:
		print("nao")
		print()
		

