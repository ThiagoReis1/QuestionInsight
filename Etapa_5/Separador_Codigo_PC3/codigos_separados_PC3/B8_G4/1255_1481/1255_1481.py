from numpy import*

v = array(eval(input("noossa:")))

a = min(v)
b = max(v)

c = (0.65*a) + (0.35*b)
d = (0.45*a) + (0.55*b)

m = array(zeros(2, dtype = int))
for i in range(size(v)):
	if(v[i] >= a and v[i] < c):
		m[0]= m[0] + 1
	elif(v[i]>= c and v[i] < d):
		m[1] = m[1] + 1
print(m)		
		
			