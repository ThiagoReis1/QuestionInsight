p = float(input("negocio: "))
op = input("negoicio: ").upper()

if (op=="C"):
	a = int(input("em quantas vezes:"))
	if (a == 1):
		print(round(p, 2))
	else:
		a = p+((8/100)*p)
		print(round(a, 2))
elif (op=="P"):
	a = p-((13/100)*p)
	print(round(a, 2))
else:
	a = p-((13/100)*p)
	print(round(a, 2))