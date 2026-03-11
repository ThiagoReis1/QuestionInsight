from numpy import*
x = array(eval(input("ss: ")))
a = min(x)
b = max(x)
c = 0.7*a+0.3*b
d= 0.4*a+0.6*b
p= 0
q = 0
for i in x:
	if(i>=c and i<d):
		p = p+1
	if(i>= d and i<b):
		q = q + 1
z = array([p,q])
print(z)
		
		