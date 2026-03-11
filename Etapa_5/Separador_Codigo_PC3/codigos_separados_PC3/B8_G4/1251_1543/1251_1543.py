#UNIVERSIDADE FEDERAL DO AMAZONAS
#VANESSA FRANCLIN GARCIA
#MATÍCULA - 21602343	
#AVALIAÇÃO 06
#01/09/2016

from numpy import*

v = array(eval(input("")))
a = min(v)
b = max(v)
c = ((0.7 * a) + (0.3 * b))
d = ((0.4 * a) + (0.6 * b))
x = array(zeros(2, dtype = int))
u = 0
m = 0
for i in range(size(v)):
	if((v[i] >= c ) and (v[i] < d)):
		u = u + 1
		x[0] = u
	elif((v[i] >= d) and (v[i] < b)):
		m = m + 1
		x[1] = m
print(x)
   
      
    
 