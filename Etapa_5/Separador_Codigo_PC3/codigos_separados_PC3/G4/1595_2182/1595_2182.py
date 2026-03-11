from numpy import *
v = array(eval(input(" v:")))
m = sum(v) 
a = min(v)
x = size(v) - 1
valor = (m - a)/ x

print(round(valor, 2))