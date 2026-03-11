from numpy import *

f = array(eval(input()))
cont = 0
n =0

for i in range(size(f)):
	if f[i] < 70 :
		cont += 1
		

s = zeros(cont, dtype= int)
for i in range(size(f)):
	if f[i] < 70:
		s[n] = i
		n = n + 1
		
		
print(cont)
print(s)
