g = float(input('peso da encomenda:'))
if(g<=4999.9):
	x = g*0.05
	print(round(x, 2))
if(g>=5000.0):
	y = ((g*0.4)/10)+60
	print(round(y, 2))
