from numpy import *

v = array(eval(input("vain :")))

i=0
n=0

while(i < size(v)):
	if(v[i] < 50):
		n = n+1
	i=i+1  
m = array(zeros(n, dtype = float))
k=0
l=0
while(k < size(v)):
	if(v[k] < 50):
		m[l] = v[k]
		l = l+1
	k = k+1
print(m)          
          