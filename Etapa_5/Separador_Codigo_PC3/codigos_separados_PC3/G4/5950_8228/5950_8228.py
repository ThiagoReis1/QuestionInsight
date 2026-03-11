it = str(input("item consumido:(P/T) "))
q = int(input("quantidade: "))
c = int(input("quantos capuccinos: "))
c1 = (5 * q) + (c * 4.5)
c2 = (6 * q) + (c * 4.5)
if (it.upper() == "P"):
	print(c1)
if (it.upper() == "T"):
	print(c2)
	