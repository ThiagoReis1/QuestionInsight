from numpy import *
v = array(eval(input()))
soma = 1
for i in range(size(v)):
	soma *= v[i]
media = soma**(1/size(v))
print(round(media,2))