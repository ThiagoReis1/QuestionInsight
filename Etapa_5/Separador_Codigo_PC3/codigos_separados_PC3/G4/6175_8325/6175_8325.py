x=float(input("variavel x: "))
import math
if((x>=-4) and (x<0)):
	print(round(abs(x**(1/2)),4))
elif((x>=0) and (x<=4)):
	print(round(math.sqrt(x),4))
else:
	print("entrada invalida")