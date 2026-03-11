from numpy import *
v = array(eval(input()))
A = min(v)
B = max(v)
C = 0.6 * A + 0.4 * B
D = 0.3 * A + 0.7 * B

for i in v :
	if (i>=A and i<C):
		v[0]+=1
	elif(1>=0 and i<B):
		v[1]+=1
		
v2 = zeros(2, dtype = 'int')
print (v)
