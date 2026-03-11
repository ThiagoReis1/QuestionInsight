from numpy import*

v = array(eval(input("vetor: ")))

c = 1
for i in range(size(v)):
	if(i <= c):
		v[i] = v[i] * c
		c = c + 1
		
print(sum(v))