from numpy import*
v = eval(input("vetor v: "))
A = min(v)
B = max(v)
C = 0.65 * A + 0.35 * B
D = 0.45 * A + 0.55 * B
x = zeros(2, dtype = int)
for i in range (size(v)):
	if (v[i] >= A) and (v[i] < C):
		x[0] = x[0] + 1
	if (v[i] >= C) and (v[i] < D):
		x[1] = x[1] + 1
print(x)