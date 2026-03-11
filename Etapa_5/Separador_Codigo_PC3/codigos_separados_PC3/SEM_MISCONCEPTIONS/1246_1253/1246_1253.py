from numpy import*
v = array(eval(input("digite o vetor:")))
A = max(v)
B = min(v)
C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B
v2 = array(0,0)
for i in range(0,size(v2)):
		if(v[i] <= A and v[i] < C):
			v2(0) = v2(0) + 1
		elif(v[i] <= B  and v[i] < D):
			v2(0) = v2(0) + 1
print(v2)