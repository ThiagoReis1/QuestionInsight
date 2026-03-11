a = int(input())
p = input()

if a <= 2005 and p.upper() == "B" or a <= 2007 and p.upper() == "E":
	print("sim")
	x = 2023 - a
	if p.upper() == "B":
		y = x - 18
		print(y)
	else:
		y = x - 16
		print(y)
elif a > 2005 and p.upper() == "B" or a > 2007 and p.upper() == "E":
	print("nao")
	x = (2023 - a)
	if p.upper() == "B":
		y = 18 - x
		print(y)
	else:
		y = 16 - x
		print(y)
else:
	print("invalido")