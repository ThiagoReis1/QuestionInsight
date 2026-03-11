q = float(input("clientes: "))
if q < 7:
	d = q*100+15
elif q == 7:
	d = q*100+12
else:
	d = q*100+10
print(round(d, 2))