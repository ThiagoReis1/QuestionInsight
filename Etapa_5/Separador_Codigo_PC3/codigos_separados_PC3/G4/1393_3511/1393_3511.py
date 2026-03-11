p = float(input("peso da encomenda:"))
c1 = (p * 0.05)
c2 = (p * 0.04) + 60
if(p<=4999.9):
	m=c1
else:
	m=c2
print(round(m,2))