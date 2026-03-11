R= 7.00
M= 6.00
B= 3.00
O= 5.00
qtr = float(input())
qtm= float(input())
qtb= float(input())
qto= float(input())
tt= qtr *R + qtm *M + qtb* B + qto *O
if tt <= 42.0 : 
	vs= tt - 3
else:
	vx= tt* (10/100)
	vs= tt - vx
	
print(vs, "ryous")	
