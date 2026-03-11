from numpy import*

v = array(eval(input("digite o vetor v:")))
A=min(v)
B=max(v)

C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B

x1 = 0
x2 = 0
for i in range(0, size(v)):
	if(C <= v[i] and v[i] <  D):
			x1 = x1 + 1
	elif(D <= v [i] and v[i] < B):
			x2 = x2 + 1
x = array([x1,x2])
print(x)
