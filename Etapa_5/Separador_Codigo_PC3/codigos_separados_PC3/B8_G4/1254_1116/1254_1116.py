from numpy import*
v = array(eval(input("Informe o vetor")))
x = array(zeros(2,dtype = int))
a = min(v)
b = max(v)
c = 0.6*a + 0.4*b
d = 0.3*a+0.7*b
for i in range(size(v)):
	if(v[i] >= c and v[i] < d):
		x[0] = x[0] + 1
	elif(v[i] >= d and v[i] < b):
		x[1] = x[1] + 1
print(x)