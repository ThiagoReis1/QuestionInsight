from numpy import *
m = array(eval(input("Insira as nostas: ")))
p = array([1,3,2,5])
t = 0
i = 0

while i < size(m):
	t = t + (m[i] * p[i])
	i += 1

me = t/11
print(round(me,2))
