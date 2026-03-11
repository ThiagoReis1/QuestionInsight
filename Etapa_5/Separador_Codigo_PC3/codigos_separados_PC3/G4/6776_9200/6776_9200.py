n = int(input("digite n: "))
p = input("digite B/R: ").upper()

i1 = (2023 - n)
if (p == "B"):
	if (i1 >= 18):
		a1 = (i1 - 18)
		print("sim")
		print(a1)
		
	else:
		n1 = (18-i1)
		print("nao")
		print(n1)
		
elif (p == "R"):
	if (i1 >= 17):
		a2 = (i1 - 17)
		print("sim")
		print(a2)
		
	else:
		n2 = (17-i1)
		print("nao")
		print(n2)
		
else:
	print("invalido")