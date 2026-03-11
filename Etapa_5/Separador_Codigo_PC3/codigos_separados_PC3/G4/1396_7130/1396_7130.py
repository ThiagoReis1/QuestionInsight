vc = float(input(""))

if vc <= 300:
	g = (vc * 10)/100
	vt = vc + g

	
else:
	g = (vc * 6)/100
	vt = vc + g
	
print(round(vt, 2))