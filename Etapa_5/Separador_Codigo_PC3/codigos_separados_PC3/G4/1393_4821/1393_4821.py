p = float(input("peso da encomenda:"))

if(p >= 5000):
	m = (p*0.04 + 60)
else:
	m = (p*0.05)
print(round(m,2))