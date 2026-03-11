m = input( )
p = float(input( ))
q = int(input( ))

d = (p*q)*0.80
s = p*q

if(m == "S"):
	print(round(d, 2))
else:
	print(round(s, 2))