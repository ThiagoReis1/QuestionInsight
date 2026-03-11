from numpy import *

v = array(eval(input("Digite as temperaturas:")))

i = 0
j = 0
while i<size(v) :
	if v[i]<0 or v[i]>40: 
		j = j + 1
	i = i + 1

v0 = array(zeros(size(v)-j, dtype=float))

i = 0
k = 0
while i<size(v) :
	if v[i]>=0 and v[i]<=40 :
		v0[k] = v[i]
		k = k + 1
	i = i + 1
print(v0)