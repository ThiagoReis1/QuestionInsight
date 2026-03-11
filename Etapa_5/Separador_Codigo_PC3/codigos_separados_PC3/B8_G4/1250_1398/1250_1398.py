from numpy import *
v = array(eval(input("")))
B = max(v)
A  =min(v)
C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B
v = zeros(2, dtype = int)
for i in vetor:
	if(i >= A) and (i < C):
		v[0]+=1
	elif(i >=B) and (i < D):
		v[1]+=1
print(v)


	