v = int (input("virus:"))
l = int (input("leucocitos:"))
taxav = float (input ("taxa de virus:"))
taxal = float (input ("taxa de leucocitos:"))

tv = taxav/100
tl = taxal/100
v = v + (v * tv)
l = l + (l * tl)
i = 1

while(v >= 2*l):
	v = v + (v * tv)
	l = l + (l * tl)
	i = i + 1
print(i)