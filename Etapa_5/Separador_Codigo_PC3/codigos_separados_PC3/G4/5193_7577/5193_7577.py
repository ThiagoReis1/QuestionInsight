qr = float(input("ramem: "))
qm = float(input("menma: "))
qb = float(input("bolinho de arroz: "))
qo = float(input("onigi: "))
r = 7.00
m = 6.00
b = 3.00
o = 5.00		
var = 42.00 

x = r*qr + m*qm + b*qb + o*qo 
if(x <= var): 
	var1 = x - 3.00 
	print(round(var1,2),"ryous")
else:
	var1 = x - (x*0.1) 
	print(round(var1,2), "ryous") 