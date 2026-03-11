from numpy import *
ve = array(eval(input()))
vs = array(eval(input()))

a = sum(ve)
b = sum(vs)
t = a - b

if(t <= 75):
	print(t)
else:
	print("Lotacao excedida")