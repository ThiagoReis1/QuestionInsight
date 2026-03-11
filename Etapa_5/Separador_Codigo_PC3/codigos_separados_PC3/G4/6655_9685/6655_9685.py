from numpy import *
x = array(eval(input("Notas: ")))
y = array([5,1])

i = 0
s = 0
t = size(x)-1
while i <= t:
		s = s + x[i]*y[i]
i += 1
		
m = s/sum(y)
print(round(m, 2))