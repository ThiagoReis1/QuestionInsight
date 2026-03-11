from numpy import*
p = 100
b1 = array([1,2,3,4,5,6])
b2 = array([1,2,1/3,4,1/5,6])
v = array(eval(input(': ')))
i = c =0
while i < size(v):
	while c < size(b1):
		if v[i]== b1[c]:
			p *= b2[c]
		c += 1
	i +=1 
	c = 0
print(round(p,2))