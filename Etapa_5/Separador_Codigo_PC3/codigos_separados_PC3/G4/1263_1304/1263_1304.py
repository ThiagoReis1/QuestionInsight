from numpy import *
p = float(input(""))
x = array(eval(input("")))
y = array(eval(input("")))
t = (p)/ (p + 1)
x = 2 * x
y = 3 * y
norma = 0
for i in range(size(x)):
	norma = ((abs(x[i] + y[i])) ** t) + norma
norma = (norma ** (1/t))
print(round(norma,7))