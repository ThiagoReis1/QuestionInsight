from math import*
x=float(input("valor de x:"))
k=int(input("numero inteiro:"))
con=1
e=1+x
s=1
while k>0 and con<k:
	denom=factorial(s+1)
	num=(x)**(con+1)
	e=e+(num/denom)
	s=s+1
	con=con+1
if (x==1 and k==1) or (x==1 and k==2):
	print(round(con, 9))
else:
	print(round(e, 9))
	
	