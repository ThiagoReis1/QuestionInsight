from numpy import*

v = array(eval(input("digite o vetor:")))

A = min(v)
B = max(v)

C = 0.6 * A + 0.4 * B

D = 0.3 * A + 0.7 * B

x = array(zeros(2, dtype = int))

for i in range (size(v)):
	if(v[i] >= A and v[i] < C):
		x[0] = x[0] + 1
	elif(v[i] >= D and v[i] < B):
		x[-1] = x[-1] + 1
		
print(x)

