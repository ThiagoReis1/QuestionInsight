pe = float(input("pe:"))


if (pe >= 5000.0):
	p = pe * 0.04 + 60
	
else:
	p = pe * 0.05
	
print(round(p, 2))
