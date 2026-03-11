vendas=float(input())

if (vendas<=1000):
   s=vendas*5/100
   print(round(s, 2))
else:
	x=vendas-1000
	y=x*10/100
	s=y+50
	
	print(round(s, 2))