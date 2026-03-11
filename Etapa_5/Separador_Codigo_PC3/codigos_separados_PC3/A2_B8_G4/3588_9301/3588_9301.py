from numpy import *
anel = array(eval(input("digite o valor: ")))
pont = 10000
for i in anel:
	if i == 1:
		pont *= 2
	elif i == 2:
		pont = pont
	elif i == 3:
		pont /= 2
	elif i == 4:
		pont /= 4
print(pont)		
		