esq = input("torta T ou pastel P: ")
qnt = int(input("fatias: "))
cpp = int(input("quantos cappuccinos: "))

c = cpp * 4.50

if esq.upper() == "T":
	pf = c + (qnt * 6)
else:
	pf = 5 * qnt + c
print(pf)
	