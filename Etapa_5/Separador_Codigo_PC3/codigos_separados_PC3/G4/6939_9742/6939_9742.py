n = float(input("valor: "))
c = input("tipo: ").upper()

d = n-n*(19/100)
s = n+n*(9/100)

if c=="C":
	num = int(input("1 ou 2: "))
	if num==2:
		print(round(s,2))
	else:
		print(round(n,2))
else:
	print(round(d,2))