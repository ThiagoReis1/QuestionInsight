from numpy import *

s = array(eval(input("cpf :")))

v = array([1,2,3,4,5,6,7,8,9])

i = 0 
t = 0

while i < len(s):
	t = t + v[i]*s[i]
	i = i + 1

d = t%11
print(d)