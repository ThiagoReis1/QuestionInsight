n = input().lower()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
if((n == "histidina") or (n == "leucina") or (n == "lisina")):
	if(n == "histidina"):
		a = (C * 6 + H * 10 + N * 3 + O * 2)
		print(round(a, 2))
	elif(n == "leucina"):
		a = (C * 6 + H * 13 + N + O *2)
		print(round(a, 2))
	elif(n == "lisina"):
		a = (C * 6 + H * 15 + N * 2 + O * 2)
		print(round(a, 2))
	else:
		print("Entrada:", n)
		print("Dado Invalido")
else:
	print("Entrada:", n)
	print("Dado Invalido")