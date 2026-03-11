from numpy import *

v = array(eval(input("Notas? ")))
vn = array([3, 2, 4, 1, 3])

i = 0
s = 0

while i < size(v):
	s = s + v[i] * vn[i]
	i = i + 1
total = s/sum(vn)
print(round(total, 2))