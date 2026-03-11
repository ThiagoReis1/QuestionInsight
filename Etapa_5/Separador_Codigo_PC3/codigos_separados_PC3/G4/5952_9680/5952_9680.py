x1 = input("")
x2 = int(input(""))
x3 = int(input(""))

pt = 3.50
ps = 5.00
pa = 13.00

xt = (x2*pt)+(x3*pa)
xs = (x2*ps)+(x3*pa)

if x1 == "S":
	print(round(xs, 2))
else:
	print(round(xt, 2))