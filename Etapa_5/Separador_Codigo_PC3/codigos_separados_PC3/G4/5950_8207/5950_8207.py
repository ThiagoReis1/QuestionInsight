i=input("(T) torta ou (P)pastel")
if i =="T":
	tt= float(input("torta: "))
	c= float(input("cap: "))
	q= (6.00 * tt) + (4.50 * c)
	print(round(q, 1))
else:
	p= float(input("pastel: "))
	cc= float(input("capp: "))
	qq= (p*5.00)+(cc*4.50)
	print(round(qq, 1))