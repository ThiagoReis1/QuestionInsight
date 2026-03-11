from math import*

x = float(input("Informe o valor de x: "))

if(x <= -1 or x>= 1):
	print(round(sqrt(abs(x)),2))
elif((x > -1 and x < 0) or (x > 0 and x < 1)):
	print(round(abs(x),2))
else:
	print(round(0,2))