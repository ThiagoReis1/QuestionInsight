a = int(input("Ano"))
p = input("B ou C").upper()
2023
if (p=="B" and a<2002):
	ap = 2002-a
	print("sim")
	print(ap)
elif (p=="C" and a<1999):
	ap = 1999-a
	print("sim")
	print(ap)
elif (p=="B" and a>2002):
	ap = a-2002
	print("nao")
	print(ap)
elif (p=="C" and a>1999):
	ap = a-1999
	print("nao")
	print(ap)
else:
	print("invalido")