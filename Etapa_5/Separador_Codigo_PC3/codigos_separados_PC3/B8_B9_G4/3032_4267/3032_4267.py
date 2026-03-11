from math import *
x = float(input("Digite o valor de x: "))
if(x<=0):
	x=0
	print(x)
else:
	if(x>0 and x<=1):
		x=1
		print(x)
	else:
		if(x>1 and x<=2):
			x=(x**(0.5))
			print(round(x,4))
		else:
			if(x>2):
				x=(x**(1/3))
				print(round(x,4))