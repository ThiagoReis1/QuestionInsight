#LETICIA DANTAS - 21601436

from numpy import*

v = array(eval(input("Insira: ")))
A = min(v)
B = max(v)
C = (0.75 * A) + (0.25 * B)
D = (0.25 * A) + (0.75 * B)
v1 = array(zeros(2, dtype = int))
p = 0
q = 0

for x in range(size(v)):
	if((v[x] >= A) and (v[x] < C)):
		q = q + 1
		v1[0] = q
	elif((v[x] >= D) and (v[x] < B)):
		p = p + 1
v1[1] = p
print(v1)