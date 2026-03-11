a = int(input("A: "))
p = input("J ou B? ").upper()
i = 2023 - a
if p == "B":
	if i >= 18:
		print("sim")
		print(2005 - a)
	else:
		print("nao")
		print(a - 2005)
elif p == "J":
	if  i >= 16:
		print("sim")
		print(2007 - a)
	else:
		print("nao")
		print(a - 2007)
else:
	print("invalido")