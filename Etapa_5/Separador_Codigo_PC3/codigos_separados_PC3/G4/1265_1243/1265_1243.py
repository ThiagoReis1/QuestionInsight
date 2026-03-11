from numpy import*
from math import*

p = float(input("digite p: "))
x = array(eval(input("digite x: ")))
y = array(eval(input("digite y: ")))

t = p/(p-1)
z = ((2*x)**t)**1/t+((3*y)**t)**1/t


print(abs(z))
	


		
		


