aluna = 1.65
tluna = 0.02
ap = round(float(input("altura da pessoa > ")),2)
tp = round(float(input("taxa de crescimento > ")),2)

a = 0

while ap < aluna:
	ap = ap + tp
	aluna = aluna + tluna
	a = a +1
print(a)