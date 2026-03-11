pv = int(input("pontos de vida:"))
d1 = int(input("D1: "))
d2 = int(input("D2: "))
d3 = int(input("D3: "))
pd = (10 * (d1 + d2 + d3))
pt = pv - pd

if (pt > 0):
	print(pt)
	print("VIVO")
else:
	pt = 0
	print(pt)
	print("MORTO")