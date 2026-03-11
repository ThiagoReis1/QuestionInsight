min = float(input())


pab = 1.20 * min
pac = 25 + 1.40 * min

pab1 = round(pab, 1)
pac1 = round(pac, 1)
if(min <= 100):
	print(pab1)
else:
	print(pac1)

