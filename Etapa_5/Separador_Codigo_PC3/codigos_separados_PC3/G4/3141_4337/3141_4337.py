from numpy import *
n = array(eval(input()))

cont = 0
total = 0

while(cont < size(n)):
	total = total + n[cont]**(1/6)
	cont = cont + 1
x = (total/size(n))**6
print(round(x,2))
