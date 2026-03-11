n = int(input(""))
pais = input("B ou R: ")
if (2023-n) >= 18 and pais == "B":
	print("sim")
	print((2023-n)-18)
	if (2023-n) >= 21 and pais == "R":
		print("sim")
		print((2023-n)-21)
	else:
		print("nao")
		print(18-(2023-n))
else:
	print("nao")
	print(21-(2023-n))