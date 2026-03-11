x = float(input())
c = input().upper()

if c == "B" or c == "R":
	y = 2023 - x
	if c == ("B"):
		if y >= 21:
			print("sim")
			print(int(y - 21))
		else:
			print("nao")
			print(int((y - 21) * -1))
	else:
		if y >= 18:
			print("sim")
			print(int(y - 18 ))
		else:
			print("nao")
			print(int((y - 18)* - 1 ))
else:
	print("invalido")