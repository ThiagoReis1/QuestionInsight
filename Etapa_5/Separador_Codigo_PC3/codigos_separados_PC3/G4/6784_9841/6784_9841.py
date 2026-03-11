n = int(input())
p = str(input()).upper()
if p == "B":
	if (2023-n) >= 21:
		print("sim")
		print(2023-n)
	else:
		print("nao")
		print(((2023-n)-21)*-1)
elif p == "R":
	if (2023-n) >= 18:
		print("sim")
		print((2023-n)-18)
	else:
		print("nao")
		print((2023-n)- 21)
else:
	print("invalido")
