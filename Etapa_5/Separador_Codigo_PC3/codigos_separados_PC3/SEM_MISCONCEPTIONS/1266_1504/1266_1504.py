from numpy import* 
from math import* 
n = 1.4539744685874278
x = array([24.30825593,-7.41203298,13.96327648])
y = array([-13.36976405,13.24149741,-28.93832117])
t = n / abs(n - 1)
c = 0
d = 0
norma = 0			 
for i in range (size(x)):
	c = c + abs(x[i])** t)
for k in range (size(y)):
	d = d + abs(y[i])**t)	
b = c ** 1/t			 
b2 = d ** 1/t
norma = 7 * abs(b - b2)			 
print(round(norma , 6))			 