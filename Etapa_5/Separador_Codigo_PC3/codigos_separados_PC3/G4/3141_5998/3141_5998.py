from numpy import * 
v = array(eval(input()))

sup = 0

for i in range(0,size(v)):
	sup = v[i]**(1/6)+sup
m = (sup/size(v))**6
print(round(m,2))