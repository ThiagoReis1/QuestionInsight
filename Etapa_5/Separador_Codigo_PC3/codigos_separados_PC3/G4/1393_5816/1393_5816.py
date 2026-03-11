#entrada
p = float(input(""))
if p >= 5000:
	s = p * 0.04 + 60
	print(round(s,2))
else:
	s = p * 0.05
	print(round(s,2))