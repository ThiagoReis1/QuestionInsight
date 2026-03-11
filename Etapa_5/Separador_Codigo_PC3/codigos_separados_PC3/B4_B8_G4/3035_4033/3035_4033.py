from math import*

x=float(input("Valor do angulo: "))

if((x>=0) and (x<90)):
	print(round(sin(radians(x)),4))
elif((x>=180) and (x<270)):
	print(round(sin(radians(x)),4))
elif((x>=90) and (x<180)):
	print(round(cos(radians(x)),4))
elif((x>=180) and (x<360)):
	print(round(cos(radians(x)),4))