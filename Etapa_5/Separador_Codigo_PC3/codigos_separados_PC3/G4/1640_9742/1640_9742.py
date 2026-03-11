from numpy import *

n = array(eval(input("N: ")))
im = 0 

for i in n:
	if i%2!=0:
		im+=1
print(im)


v = zeros(im, dtype=int)
z = 0 
for i in range(size(n)):
	if n[i]%2!=0:
		v[z]=i
		z+=1
print(v)