v = float(input("valor:"))
c = input("codigo:").upper()

if c =="D":
	d = v - (18/100)*v
elif c == "P":
	d = v - (18/100)*v
else:
	p = int(input("parcelas:"))
	if p == 1:
		d = v
	else:
		d = v +(7/100)*v
print(round(d, 2))
		
	