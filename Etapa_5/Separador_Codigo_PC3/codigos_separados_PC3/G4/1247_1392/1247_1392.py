from numpy import*
v = array(eval(input("vetor: ")))

A = min(v)
B = max(v)

C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B

x = zeros(2, dtype = int)
l = 0
x1 = 0
x2 = 0
for l in v(0, size(v)):
	if(v[l] >= A and v[l] < C):
		x1 = x1 + 1
	if(v[l] >= D and v[l] < B):
		x2 = x2 + 1
x[0] = x1
x[1] = x2
print(x)
			
