a = float(input("quant de ramem: "))
b = float(input("quant de menma: "))
c = float(input("quant de arroz: "))
d = float(input("quant de onigi: "))
if (7*a)+(6*b)+(3*c)+(5*d)<=42:
	res = ((7*a)+(6*b)+(3*c)+(5*d))-3 
	print(round(res,2) ,"ryous")
else: 
	res = 0.90*((7*a)+(6*b)+(3*c)+(5*d)) 
	print(round(res,2) ,"ryous")