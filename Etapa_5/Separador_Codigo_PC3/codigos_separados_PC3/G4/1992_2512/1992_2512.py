a = input().lower()

if(a == "glutamina"):
	p = (12.011 * 5 + 1.00794 * 8 + 14.00674 * 1 + 15.999 * 4)
	print(round(p,2))
elif(a == "histidina"):
	p = (12.011 * 6 + 1.00794 * 10 + 14.00674 * 3 + 15.999 * 2)
	print(round(p,2))
elif(a == "prolina"):
	p = (12.011 * 5 + 1.00794 * 10 + 14.00674 * 1 + 15.999 * 2)
	print(round(p,2))
else:
	print("Entrada: ", a)
	print("Dado Invalido")
