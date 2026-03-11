from numpy import*
from numpy.linalg import*

t = array(eval(input("t: ")))
q = 0

for x in t:
	if(x % 5 == 0):
		q += 1

t_2 = zeros(q, dtype = int)
q_2 = 0

for i in range(size(t)):
	if(t[i] % 5 == 0):
		t_2[q_2] = i
		q_2 += 1
print(q_2)
print(t_2)