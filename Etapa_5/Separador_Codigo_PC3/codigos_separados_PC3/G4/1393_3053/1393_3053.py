p = float(input("peso da encomenda: "))
x = (p*5)/100
y = ((p*4)/100) + 60
if (p>=5000):
	v = y
else:
	v = x
print(round(v,2))