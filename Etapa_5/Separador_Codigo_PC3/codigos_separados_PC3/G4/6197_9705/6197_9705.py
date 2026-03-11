aa = 1.6
ta = 0.02
ap = float(input("digite ap: "))
tp = float(input("digite tp: "))
anos = 0

while aa > ap:
	aa = aa + ta
	ap = ap + tp
	anos = anos + 1
print(anos)
