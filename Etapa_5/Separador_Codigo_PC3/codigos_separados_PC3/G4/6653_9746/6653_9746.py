from numpy import *

t = array(eval(input()))

x = t[0] * 3 + t[1] * 5 + t[2] * 1
y = x/(3+5+1)

print(round(y, 2))