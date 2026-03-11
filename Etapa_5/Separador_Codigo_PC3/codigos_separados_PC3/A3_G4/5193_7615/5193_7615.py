qr= float(input("quantidade de ramem:"))
qm= float(input("quantidade de menma:"))
qba= float(input("quantidade de bolinho de arroz:"))
qo= float(input("quantidade de onigi:"))
vqr=7.00
vqm=6.00
vqba=3.00
vqo=5.00
vt2= (qr *7.00) + (qm * 6.00) + (qba*3.00) + (qo*5.00)
c= 42.00
v= 3.00
v1= (10/100)

if(vt2 <= c):
	total=(vt2 - v)
else:
	total=(vt2 - (vt2 * v1))
	
print((round(total,2)), "ryous")