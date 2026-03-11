from numpy import*
v = array(eval(input("digite")))
b = 0
for i in range(size(v)):
	if v[i] > 160:
		v[i] = v[i] - 25
		
		
print(round(sum(v), 2))
		