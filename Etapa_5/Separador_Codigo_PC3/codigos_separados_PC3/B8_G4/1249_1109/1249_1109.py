from numpy import*
v = array(eval(input("Digite o vetor: ")))
A = min(v)
B = max(v)
C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B
x = zeros(2, dtype = int)
for i in range(size(v)):
	if(v[i] >= A and v[i] < C):
		x[0] = x[0] + 1
	elif(v[i] >= C and v[i] < D):
		x[1] = x[1] + 1
print(x)