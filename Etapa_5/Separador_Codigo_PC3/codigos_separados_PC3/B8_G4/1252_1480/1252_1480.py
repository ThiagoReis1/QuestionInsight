#UFAM
#Pedro Vinícius Borges - Engenharia Química - 21650221

from numpy import*

v = array(eval(input("vetor v: ")))

A = min(v)
B = max(v)
			 
C = 0.6 * A + 0.4 * B
D = 0.3 * A + 0.7 * B
cond_1 = 0
cond_2 = 0 
for i in v:
	if i >= A and i < C:
		cond_1 += 1
	elif i >= C and i < D:
		cond_2+=1
x = zeros(2, dtype = int)
x[0] = cond_1
x[1] = cond_2
print(x)
	