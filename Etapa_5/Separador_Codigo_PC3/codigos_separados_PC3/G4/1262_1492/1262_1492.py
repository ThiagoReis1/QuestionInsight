from numpy import *
a = float(input(""))
x = array(eval(input("")))
y = array(eval(input("")))
l = (a) / (a - 1)
j = 0
for i in range(size(x)):
  	j = (abs(x[i] - y[i]) ** l) + j
j = ( j ** (1/l))
print(round(j, 6))