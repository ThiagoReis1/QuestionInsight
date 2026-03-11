from numpy import*
v = array(eval(input("numeros")))
x = zeros(2,dtype = int)
A =  min(v)
B =  max(v)
C = 0.6*A+0.4*B
D = 0.3*A+0.7*B
x1 = 0
x2 = 0
for i in v:
	if (i >= A and i < C):
		x1 = x1+ 1
	if (i >= D and i < B):
		x2 = x2 + 1
x[0] = x1
x[1]  = x2
print (x)