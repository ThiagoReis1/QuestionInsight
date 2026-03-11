p = float(input("peso da encomenda: "))

if (p0 <= 4999.9):
	msg = (p*0.05)+60
else:
	msg = (p*0.04)+60
print(round(msg,2))