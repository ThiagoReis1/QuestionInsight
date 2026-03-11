from numpy import*

v = eval(input("saques:"))

s = []
p = 0

for i in range(size(v)):
	if(v[i]<=50):
		p = p + 1
		s.append(i)
		
print(p)
print(array(s))