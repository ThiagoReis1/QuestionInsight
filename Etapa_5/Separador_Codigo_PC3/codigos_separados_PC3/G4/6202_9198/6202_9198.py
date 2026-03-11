ab = 1.69
tb = 0.01
ap = float(input("Altura: "))
tp = float(input("Taxa: "))
c = 0

while(ab > ap):
	ab = ab + tb
	ap = ap + tp
	c += 1
print(c)