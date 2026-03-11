from numpy import*
v = array(eval(input("Digite os valores:")))

A = min(v)
B = max(v)
C = 0.6 * A + 0.4 * B
D = 0.3 * A + 0.7* B

x = zeros(2, dtype = int)

for i in range(size(v)):
	if (v[i] >= C and v[i] < D):
		x[0] = x[0] + 1
	elif (v[i] >= D and v[i] < B):
		x[1] = x[1] + 1

print(x)
		