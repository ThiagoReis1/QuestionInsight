v = float(input("valor total da compra: "))
c = input("D P ou C:")
z = 1 or 2
if c == "D":
	a = v-(v*0.13)
	print(round(a, 2))
elif c == "P":
	b = v-(v*0.13)
	print(round(b, 2))
else:
	z=int(input())
	if z == 1:
		d = v
		print(round(v, 2))
	if z == 2:
		e = v+(0.08*v)
		print(round(e, 2))
