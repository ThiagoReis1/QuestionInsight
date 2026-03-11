from numpy import *
x = array(eval(input("vetor: ")))
A = min(x)
B = max(x)
C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B
j = 0
k = 0
for i in x:
	if (i >= A and i < C):
		j = j + 1
	if (i >= D and i < B ):
		k = k + 1
t = array([j , k])
print(t)